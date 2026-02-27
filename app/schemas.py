from pydantic import BaseModel, Field

class GenerationRequest(BaseModel):
    prompt: str = Field(
        ...,
        min_lenght=1,
        json_schema_extra={
            "example" : "Explain Quantum Physics"
        }
    )

    max_tokens: int = Field(
        256,
        ge=10,
        le=1024,
        json_schema_extra={
            "example" : 128
        }
    ) 

    temperature: float = Field(
        0.7,
        ge=0.0,
        le=1.0,
        json_schema_extra={
            "example" : 0.7
        }
    )

class GenerationResponse(BaseModel):
    result: str
    token_usage: int