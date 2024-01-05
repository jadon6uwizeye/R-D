from fastapi import FastAPI
import EDF_format_pyEDFlib as edf
from fastapi.responses import FileResponse
from pydantic import BaseModel


app = FastAPI()


class EDF(BaseModel):
    hr: list
    spo2: list


@app.post("/edf/", status_code=200)
async def create_item(data: EDF):
    try:
        edf.write_edf(
            filename="edf_file",
            signals = [data.hr, data.spo2],
            channel_names=["hr", "spo2"],
            header=None,
        )
        return {
            "status": "OK",
            "status_code": 200,
            "message": "EDF file created successfully",
            "location": app.url_path_for("get_file", file_name="edf_file.edf"),
        }
    except Exception as e:
        return {
            "status": "ERROR",
            "status_code": 500,
            "message": "EDF file creation failed",
            "details": f"{e}",
        }            

@app.get("/sample/")
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
    try:
        print("file_name: ", file_name)
        if file_name.endswith(".edf"):
            # check if file exists
            if edf.check_file_exists(file_name):
                return FileResponse(file_name, media_type="application/octet-stream", filename=file_name)
            else:
                return {
                    "status": "Not Found",
                    "status_code": 404,
                    "message": "File not found",
                    "file_name": file_name,
                    "location": app.url_path_for("get_file", file_name=file_name),
                }
        else:
            return {
                "status": "Not Found",
                "status_code": 404,
                "message": "File not found",
                "file_name": file_name,
                "location": app.url_path_for("get_file", file_name=file_name),
            }
    except Exception as e:
        return {
            "status": "Not Found",
            "status_code": 404,
            "message": "File not found",
            "details": f"{e}",
            "file_name": file_name,
            "location": app.url_path_for("get_file", file_name=file_name),
        }
