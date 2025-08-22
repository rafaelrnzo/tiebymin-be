from fastapi.responses import JSONResponse
from typing import Any, Type, Optional, List, Dict, Union
from app.schemas.web_response import WebResponse, CustomColumn, Paging
from pydantic import BaseModel
from .serializers import CustomJSONEncoder, _serialize_sqlalchemy_obj
import json

def create_response(
    data: Any = None, 
    code: int = 200, 
    status: str = "OK",
    column: Optional[List[CustomColumn]] = None,
    paging: Optional[Union[Dict[str, int], Paging]] = None,
    errors: Optional[Dict[str, List[str]]] = None,
    metadata: Optional[Dict[str, Any]] = None,
    output_model: Optional[Type[BaseModel]] = None
) -> JSONResponse:
    response_dict = {"code": code, "status": status}
    if data is not None:
        response_dict["data"] = _serialize_sqlalchemy_obj(data, output_model)
    if column is not None and len(column) > 0:
        response_dict["column"] = column
    if paging is not None:
        if isinstance(paging, BaseModel):
            response_dict["paging"] = paging.model_dump()
        else:
            response_dict["paging"] = paging
    if errors is not None and len(errors) > 0:
        response_dict["errors"] = errors
    if metadata is not None and len(metadata) > 0:
        response_dict["metadata"] = metadata
    content_json = json.dumps(response_dict, cls=CustomJSONEncoder)
    content_dict = json.loads(content_json)
    return JSONResponse(
        content=content_dict,
        status_code=code,
        media_type="application/json"
    )

def success_response(
    data: Any = None,
    paging: Optional[Paging] = None,
    column: Optional[List[CustomColumn]] = None,
    metadata: Optional[Dict[str, Any]] = None
) -> WebResponse:
    return WebResponse(
        code=200,
        status="OK",
        data=data,
        paging=paging,
        column=column,
        metadata=metadata
    )

def created_response(
    data: Any = None,
    metadata: Optional[Dict[str, Any]] = None
) -> WebResponse:
    return WebResponse(
        code=201,
        status="Created", 
        data=data,
        metadata=metadata
    )

def error_response(
    code: int,
    status: str,
    errors: Optional[Dict[str, List[str]]] = None,
    metadata: Optional[Dict[str, Any]] = None
) -> WebResponse:
    return WebResponse(
        code=code,
        status=status,
        errors=errors,
        metadata=metadata
    )

def bad_request_response(
    errors: Optional[Dict[str, List[str]]] = None,
    metadata: Optional[Dict[str, Any]] = None
) -> WebResponse:
    return error_response(400, "Bad Request", errors, metadata)

def not_found_response(
    errors: Optional[Dict[str, List[str]]] = None,
    metadata: Optional[Dict[str, Any]] = None
) -> WebResponse:
    return error_response(404, "Not Found", errors, metadata)

def unauthorized_response(
    errors: Optional[Dict[str, List[str]]] = None,
    metadata: Optional[Dict[str, Any]] = None
) -> WebResponse:
    return error_response(401, "Unauthorized", errors, metadata)

def internal_server_error_response(
    errors: Optional[Dict[str, List[str]]] = None,
    metadata: Optional[Dict[str, Any]] = None
) -> WebResponse:
    return error_response(500, "Internal Server Error", errors, metadata) 