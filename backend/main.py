from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
import smtplib
from email.message import EmailMessage

app = FastAPI()

class FormData(BaseModel):
    name: str
    email: EmailStr
    phone: str = ""
    subject: str
    message: str

@app.post("/contact")
def contact(data: FormData):

    if not data.name or not data.message:
        raise HTTPException(status_code=400, detail="Datos inválidos")

    msg = EmailMessage()
    msg["From"] = "Web ADF <no-reply@adfglobal.com>"
    msg["To"] = "contacto@adfglobal.com"
    msg["Subject"] = f"Consulta web - {data.subject}"

    msg.set_content(f"""
Nombre: {data.name}
Correo: {data.email}
Teléfono: {data.phone}

Mensaje:
{data.message}
""")

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login("TU_CORREO@gmail.com", "APP_PASSWORD")
            server.send_message(msg)
    except:
        raise HTTPException(status_code=500, detail="Error enviando correo")

    return {"ok": True}
