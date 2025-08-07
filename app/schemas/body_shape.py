import uuid
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class BodyShapeBase(BaseModel):
    name: str = Field(..., example="Apple", description="Name of the body shape.")
    penjelasan_body_shape: str = Field(..., example="Characterized by a larger upper body and narrower hips.", description="Description of the body shape.")
    karakteristik: str = Field(..., example="Broad shoulders, full bust, and narrow hips.", description="Characteristics of the body shape.")
    tips_body_shape: str = Field(..., example="Wear A-line dresses to balance proportions.", description="Fashion tips for the body shape.")
    link_picture: str = Field(..., example="https://example.com/apple-body-shape.jpg", description="Link to an image representing the body shape.")
    is_active: bool = Field(True, description="Indicates whether the body shape is active and used.")
    
class BodyShapeCreate(BodyShapeBase):
    pass

class BodyShape(BodyShapeBase):
    id: uuid.UUID
    created_at: datetime
    updated_at: datetime
    
    class Config:
        orm_mode = True
    
    
    

# create table public.body_shapes (
#   id uuid not null default gen_random_uuid (),
#   name character varying not null,
#   penjelasan_body_shape text not null,
#   karakteristik text not null,
#   tips_body_shape text not null,
#   link_picture character varying not null,
#   is_active boolean not null default true,
#   created_at timestamp with time zone not null default now(),
#   updated_at timestamp with time zone not null default now(),
#   constraint body_shapes_pkey primary key (id)
# ) TABLESPACE pg_default;