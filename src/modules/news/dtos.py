from pydantic import BaseModel

class RssReadderDTO(BaseModel):
    url: str
