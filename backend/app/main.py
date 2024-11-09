import logging
from fastapi import FastAPI, File, UploadFile, Form, Depends
from sqlalchemy.orm import Session
from typing import List, Optional
from . import crud, models, schemas, utils
from .database import SessionLocal, engine
from fastapi.staticfiles import StaticFiles
import os

# Set up logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

@app.on_event("startup")
def on_startup():
    models.Base.metadata.create_all(bind=engine)



# Dependency to get the database session


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Mount media folder
# media_folder = os.path.join(os.getcwd(), "media")
media_folder = "D:/Projects/Task/techgyassignment/backend/media"
app.mount("/media", StaticFiles(directory=media_folder), name="media")


@app.post("/create_legality/")
async def create_legality(
    land_documents_file: List[UploadFile] = File(...),
    land_documents_comment: Optional[str] = Form(None),
    pattadhar_passbook_file: List[UploadFile] = File(...),
    pattadhar_passbook_comment: Optional[str] = Form(None),
    link_documents_file: List[UploadFile] = File(...),
    link_documents_comment: Optional[str] = Form(None),
    kasara_pahani_file: List[UploadFile] = File(...),
    kasara_pahani_comment: Optional[str] = Form(None),
    encumbrance_certificate_file: List[UploadFile] = File(...),
    encumbrance_comment: Optional[str] = Form(None),
    revenue_record_file: List[UploadFile] = File(...),
    revenue_record_comment: Optional[str] = Form(None),
    partition_deed_file: List[UploadFile] = File(...),
    partition_comment: Optional[str] = Form(None),
    faisal_patti_file: List[UploadFile] = File(...),
    faisal_patti_comment: Optional[str] = Form(None),
    death_certificate_file: List[UploadFile] = File(...),
    death_certificate_comment: Optional[str] = Form(None),
    lease_agreement_file: List[UploadFile] = File(...),
    lease_agreement_comment: Optional[str] = Form(None),
    legal_opinion_report_file: List[UploadFile] = File(...),
    legal_opinion_comment: Optional[str] = Form(None),
    land_coordinates_file: List[UploadFile] = File(...),
    land_coordinates_comment: Optional[str] = Form(None),
    owner_kyc_video_file: List[UploadFile] = File(...),
    owner_kyc_video_comment: Optional[str] = Form(None),
    db: Session = Depends(get_db)
):
    try:
        # Log the start of the request processing
        logger.info("Started processing create_legality request")

        # Save files and get file paths for each field
        land_documents_paths = utils.save_files(
            land_documents_file, "land_documents")
        pattadhar_passbook_paths = utils.save_files(
            pattadhar_passbook_file, "pattadhar_passbook")
        link_documents_paths = utils.save_files(
            link_documents_file, "link_documents")
        kasara_pahani_paths = utils.save_files(
            kasara_pahani_file, "kasara_pahani")
        encumbrance_certificate_paths = utils.save_files(
            encumbrance_certificate_file, "encumbrance_certificate")
        revenue_record_paths = utils.save_files(
            revenue_record_file, "revenue_record")
        partition_deed_paths = utils.save_files(
            partition_deed_file, "partition_deed")
        faisal_patti_paths = utils.save_files(
            faisal_patti_file, "faisal_patti")
        death_certificate_paths = utils.save_files(
            death_certificate_file, "death_certificate")
        lease_agreement_paths = utils.save_files(
            lease_agreement_file, "lease_agreement")
        legal_opinion_report_paths = utils.save_files(
            legal_opinion_report_file, "legal_opinion_report")
        land_coordinates_paths = utils.save_files(
            land_coordinates_file, "land_coordinates")
        owner_kyc_video_paths = utils.save_files(
            owner_kyc_video_file, "owner_kyc_video")

        # Prepare data to be inserted into the database
        legality_data = schemas.LegalityCreate(
            land_documents_file=land_documents_paths,
            land_documents_comment=land_documents_comment,
            pattadhar_passbook_file=pattadhar_passbook_paths,
            pattadhar_passbook_comment=pattadhar_passbook_comment,
            link_documents_file=link_documents_paths,
            link_documents_comment=link_documents_comment,
            kasara_pahani_file=kasara_pahani_paths,
            kasara_pahani_comment=kasara_pahani_comment,
            encumbrance_certificate_file=encumbrance_certificate_paths,
            encumbrance_comment=encumbrance_comment,
            revenue_record_file=revenue_record_paths,
            revenue_record_comment=revenue_record_comment,
            partition_deed_file=partition_deed_paths,
            partition_comment=partition_comment,
            faisal_patti_file=faisal_patti_paths,
            faisal_patti_comment=faisal_patti_comment,
            death_certificate_file=death_certificate_paths,
            death_certificate_comment=death_certificate_comment,
            lease_agreement_file=lease_agreement_paths,
            lease_agreement_comment=lease_agreement_comment,
            legal_opinion_report_file=legal_opinion_report_paths,
            legal_opinion_comment=legal_opinion_comment,
            land_coordinates_file=land_coordinates_paths,
            land_coordinates_comment=land_coordinates_comment,
            owner_kyc_video_file=owner_kyc_video_paths,
            owner_kyc_video_comment=owner_kyc_video_comment,
        )

        # Log the prepared data
        logger.info("Prepared legality data for database insertion")

        # Insert the data into the database
        result = crud.create_legality(db=db, legality=legality_data)

        # Log the success
        logger.info(f"Legality record created with ID {result.id}")

        return result
    except Exception as e:
        # Log any error that occurs
        logger.error(f"Error processing create_legality request: {e}")
        raise e
