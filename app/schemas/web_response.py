from typing import Any, Dict, List, Optional, TypeVar, Generic
from pydantic import BaseModel, Field

T = TypeVar("T")

class CustomColumn(BaseModel):
    field: str
    headerName: str
    width: Optional[int] = None
    # Add other custom properties as needed

    model_config = dict(from_attributes=True, exclude_none=True)

class Paging(BaseModel):
    page: int
    size: int
    totalItems: int
    totalPages: int

    model_config = dict(from_attributes=True, exclude_none=True)

class WebResponse(BaseModel, Generic[T]):
    code: int = Field(..., description="HTTP status code (e.g. 200, 201, 400, etc.)")
    status: str = Field(..., description="HTTP status text (e.g. 'OK', 'Created', 'Bad Request')")
    column: Optional[List[CustomColumn]] = Field(None, description="Dynamic column definitions for UI tables")
    data: Optional[T] = Field(None, description="The main payload (object or array)")
    paging: Optional[Paging] = Field(None, description="Pagination info, omit if not paginated")
    errors: Optional[Dict[str, List[str]]] = Field(None, description="Validation or business errors")
    metadata: Optional[Dict[str, Any]] = Field(None, description="Any additional info (e.g. requestId, executionTime)")

    model_config = dict(from_attributes=True, exclude_none=True)

    def model_dump(self, *args, **kwargs):
        kwargs.setdefault('exclude_none', True)
        result = super().model_dump(*args, **kwargs)
        # Remove keys with value None or empty list
        return {k: v for k, v in result.items() if v is not None and v != []}

    def model_dump_json(self, *args, **kwargs):
        kwargs.setdefault('exclude_none', True)
        return super().model_dump_json(*args, **kwargs)
