from fastapi import FastAPI
import EDF_format_pyEDFlib as edf
from fastapi.responses import FileResponse

app = FastAPI()


@app.get("/")
async def root():
    return {
        "status": "OK",
        "status_code": 200,
        "message": "EDF file created successfully",
        "file_name": edf.write_edf("edf_file", None, None, None),
        "location": app.url_path_for("get_file", file_name="edf_file.edf"),

    }


# serve file from fastapi
@app.get(("/{file_name}"))
async def get_file(file_name: str):
    return FileResponse(file_name)
