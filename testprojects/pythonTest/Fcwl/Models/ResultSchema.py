from pydantic import BaseModel

class FormSchema(BaseModel):
    name: str 
    fields: dict  
    description: str

class ResultSchema(BaseModel):
    name: str
    address: str
    contact_info: dict  # convert dict to custom type if needed? see how it works first
    forms: list[FormSchema]