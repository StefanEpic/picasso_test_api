from drf_spectacular.utils import extend_schema, extend_schema_view

upload_file_summary = extend_schema_view(
    create=extend_schema(
        summary="Upload file",
        description="Endpoint for upload file.",
    ),
)

get_file_summary = extend_schema_view(
    list=extend_schema(
        summary="Get list uploaded files",
        description="Endpoint for return list of uploaded files",
    ),
)
