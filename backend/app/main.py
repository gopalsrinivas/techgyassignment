import logging
from fastapi import FastAPI, File, UploadFile, Form, Depends, HTTPException
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from typing import List, Optional
from . import crud, models, schemas, utils
from .database import SessionLocal, engine
from fastapi.staticfiles import StaticFiles
import os
from pathlib import Path

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
    land_coordinates_comment_file: Optional[str] = Form(None),
    owner_kyc_video_file: List[UploadFile] = File(...),
    owner_kyc_video_comment: Optional[str] = Form(None),
    db: Session = Depends(get_db)
):
    try:
        logger.info("Started processing create_legality request")

        # Save files and get filenames
        land_documents_filenames = utils.save_files(land_documents_file, "land_documents")
        pattadhar_passbook_filenames = utils.save_files(pattadhar_passbook_file, "pattadhar_passbook")
        link_documents_filenames = utils.save_files(link_documents_file, "link_documents")
        kasara_pahani_filenames = utils.save_files(kasara_pahani_file, "kasara_pahani")
        encumbrance_certificate_filenames = utils.save_files(encumbrance_certificate_file, "encumbrance_certificate")
        revenue_record_filenames = utils.save_files(revenue_record_file, "revenue_record")
        partition_deed_filenames = utils.save_files(partition_deed_file, "partition_deed")
        faisal_patti_filenames = utils.save_files(faisal_patti_file, "faisal_patti")
        death_certificate_filenames = utils.save_files(death_certificate_file, "death_certificate")
        lease_agreement_filenames = utils.save_files(lease_agreement_file, "lease_agreement")
        legal_opinion_report_filenames = utils.save_files(legal_opinion_report_file, "legal_opinion_report")
        land_coordinates_filenames = utils.save_files(land_coordinates_file, "land_coordinates")
        owner_kyc_video_filenames = utils.save_files(owner_kyc_video_file, "owner_kyc_video")

        # Prepare data for database insertion
        legality_data = schemas.LegalityCreate(
            land_documents_file=land_documents_filenames,
            land_documents_comment=land_documents_comment,
            pattadhar_passbook_file=pattadhar_passbook_filenames,
            pattadhar_passbook_comment=pattadhar_passbook_comment,
            link_documents_file=link_documents_filenames,
            link_documents_comment=link_documents_comment,
            kasara_pahani_file=kasara_pahani_filenames,
            kasara_pahani_comment=kasara_pahani_comment,
            encumbrance_certificate_file=encumbrance_certificate_filenames,
            encumbrance_comment=encumbrance_comment,
            revenue_record_file=revenue_record_filenames,
            revenue_record_comment=revenue_record_comment,
            partition_deed_file=partition_deed_filenames,
            partition_comment=partition_comment,
            faisal_patti_file=faisal_patti_filenames,
            faisal_patti_comment=faisal_patti_comment,
            death_certificate_file=death_certificate_filenames,
            death_certificate_comment=death_certificate_comment,
            lease_agreement_file=lease_agreement_filenames,
            lease_agreement_comment=lease_agreement_comment,
            legal_opinion_report_file=legal_opinion_report_filenames,
            legal_opinion_comment=legal_opinion_comment,
            land_coordinates_file=land_coordinates_filenames,
            land_coordinates_comment_file=land_coordinates_comment_file,
            owner_kyc_video_file=owner_kyc_video_filenames,
            owner_kyc_video_comment=owner_kyc_video_comment,
        )

        logger.info("Prepared legality data for database insertion")
        result = crud.create_legality(db=db, legality=legality_data)
        logger.info(f"Legality record created with ID {result.id}")

        # Prepare the response data with success code, message, and response data
        response_data = {
            "status_code": 201,
            "message": "Legality created successfully",
            "data": {
                "id": result.id,
                "land_documents_file": result.land_documents_file,
                "land_documents_comment": result.land_documents_comment,
                "pattadhar_passbook_file": result.pattadhar_passbook_file,
                "pattadhar_passbook_comment": result.pattadhar_passbook_comment,
                "link_documents_file": result.link_documents_file,
                "link_documents_comment": result.link_documents_comment,
                "kasara_pahani_file": result.kasara_pahani_file,
                "kasara_pahani_comment": result.kasara_pahani_comment,
                "encumbrance_certificate_file": result.encumbrance_certificate_file,
                "encumbrance_comment": result.encumbrance_comment,
                "revenue_record_file": result.revenue_record_file,
                "revenue_record_comment": result.revenue_record_comment,
                "partition_deed_file": result.partition_deed_file,
                "partition_comment": result.partition_comment,
                "faisal_patti_file": result.faisal_patti_file,
                "faisal_patti_comment": result.faisal_patti_comment,
                "death_certificate_file": result.death_certificate_file,
                "death_certificate_comment": result.death_certificate_comment,
                "lease_agreement_file": result.lease_agreement_file,
                "lease_agreement_comment": result.lease_agreement_comment,
                "legal_opinion_report_file": result.legal_opinion_report_file,
                "legal_opinion_comment": result.legal_opinion_comment,
                "land_coordinates_file": result.land_coordinates_file,
                "land_coordinates_comment": result.land_coordinates_comment_file,
                "owner_kyc_video_file": result.owner_kyc_video_file,
                "owner_kyc_video_comment": result.owner_kyc_video_comment,
            }
        }

        return response_data
    except Exception as e:
        logger.error(f"Error processing create_legality request: {e}")
        return {
            "status_code": 500,
            "message": "Failed to create legality",
            "error": str(e)
        }

# Get ALL fetch all legality records
@app.get("/List_legality/", response_model=schemas.LegalityListResponse)
async def get_legality_list(db: Session = Depends(get_db)):
    try:
        # Query the database to get all legality records
        legality_records = db.query(models.Legality).all()

        if not legality_records:
            raise HTTPException(status_code=404, detail="No legality records found")

        # Convert the ORM models to Pydantic models
        legality_response = [schemas.LegalityResponse.from_orm( record) for record in legality_records]

        return {"legality": legality_response}
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"An unexpected error occurred: {str(e)}"
        )


@app.post("/create-family-tree/", response_model=schemas.FamilyTreeResponse)
async def create_family_tree_endpoint(family_tree: schemas.FamilyTreeCreate, db: Session = Depends(get_db)):
    try:
        # Creating the family tree in the database
        db_family_tree = crud.create_family_tree(db=db, family_tree=family_tree)

        response_data = schemas.FamilyTreeResponse(
            id=db_family_tree.id,
            father_name=db_family_tree.father_name,
            father_age=db_family_tree.father_age,
            mother_name=db_family_tree.mother_name,
            mother_age=db_family_tree.mother_age,
            owner_name=db_family_tree.owner_name,
            owner_age=db_family_tree.owner_age,
            religion=db_family_tree.religion,
            num_wifes=db_family_tree.num_wifes,
            num_kids=db_family_tree.num_kids,
            num_siblings=db_family_tree.num_siblings,
        )

        logger.info(f"Family tree created with ID: {db_family_tree.id}")
        return response_data
    except HTTPException as e:
        raise e
    except Exception as e:
        logger.error(f"Error in create_family_tree endpoint: {e}")
        raise HTTPException(status_code=500, detail="An error occurred while creating the FamilyTree")

        
# List endpoint to get FamilyTree records
@app.get("/list-family-tree/", response_model=schemas.FamilyTreeListResponse)
async def get_family_tree_endpoint(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    try:
        family_tree_records = crud.get_family_tree(db=db, skip=skip, limit=limit)

        response_data = schemas.FamilyTreeListResponse(
            family_tree=[schemas.FamilyTreeResponse(
                id=db_family_tree.id,
                father_name=db_family_tree.father_name,
                father_age=db_family_tree.father_age,
                mother_name=db_family_tree.mother_name,
                mother_age=db_family_tree.mother_age,
                owner_name=db_family_tree.owner_name,
                owner_age=db_family_tree.owner_age,
                religion=db_family_tree.religion,
                num_wifes=db_family_tree.num_wifes,
                num_kids=db_family_tree.num_kids,
                num_siblings=db_family_tree.num_siblings
            ) for db_family_tree in family_tree_records]
        )

        logger.info(f"Retrieved {len(family_tree_records)} FamilyTree records")
        return response_data
    except HTTPException as e:
        raise e
    except Exception as e:
        logger.error(f"Error in get_family_tree endpoint: {e}")
        raise HTTPException(
            status_code=500, detail="An error occurred while retrieving FamilyTree records")
