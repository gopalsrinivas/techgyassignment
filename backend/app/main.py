import os
import logging
from pathlib import Path
from typing import List, Optional

from fastapi import FastAPI, APIRouter, HTTPException, Depends, UploadFile, File, Form
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from . import crud, models, schemas, utils
from .database import SessionLocal, engine
from .schemas import ValuationListResponse, ValuationResponse, ApiResponse

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()


@app.on_event("startup")
def on_startup():
    models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
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


@app.get("/List_legality/", response_model=schemas.LegalityListResponse)
async def get_legality_list(db: Session = Depends(get_db)):
    try:
        legality_records = db.query(models.Legality).all()

        if not legality_records:
            raise HTTPException(status_code=404, detail="No legality records found")

        legality_response = [schemas.LegalityResponse.from_orm( record) for record in legality_records]

        return {"legality": legality_response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {str(e)}")


@app.put("/update_legality/{legality_id}")
async def update_legality(
    legality_id: int,
    land_documents_file: List[UploadFile] = File(None),
    land_documents_comment: Optional[str] = Form(None),
    pattadhar_passbook_file: List[UploadFile] = File(None),
    pattadhar_passbook_comment: Optional[str] = Form(None),
    link_documents_file: List[UploadFile] = File(None),
    link_documents_comment: Optional[str] = Form(None),
    kasara_pahani_file: List[UploadFile] = File(None),
    kasara_pahani_comment: Optional[str] = Form(None),
    encumbrance_certificate_file: List[UploadFile] = File(None),
    encumbrance_comment: Optional[str] = Form(None),
    revenue_record_file: List[UploadFile] = File(None),
    revenue_record_comment: Optional[str] = Form(None),
    partition_deed_file: List[UploadFile] = File(None),
    partition_comment: Optional[str] = Form(None),
    faisal_patti_file: List[UploadFile] = File(None),
    faisal_patti_comment: Optional[str] = Form(None),
    death_certificate_file: List[UploadFile] = File(None),
    death_certificate_comment: Optional[str] = Form(None),
    lease_agreement_file: List[UploadFile] = File(None),
    lease_agreement_comment: Optional[str] = Form(None),
    legal_opinion_report_file: List[UploadFile] = File(None),
    legal_opinion_comment: Optional[str] = Form(None),
    land_coordinates_file: List[UploadFile] = File(None),
    land_coordinates_comment_file: Optional[str] = Form(None),
    owner_kyc_video_file: List[UploadFile] = File(None),
    owner_kyc_video_comment: Optional[str] = Form(None),
    db: Session = Depends(get_db)
):
    logger.info("Started processing update_legality request")

    update_data = {}

    if land_documents_file:
        update_data["land_documents_file"] = utils.save_files(
            land_documents_file, "land_documents")
    if land_documents_comment is not None:
        update_data["land_documents_comment"] = land_documents_comment

    if pattadhar_passbook_file:
        update_data["pattadhar_passbook_file"] = utils.save_files(
            pattadhar_passbook_file, "pattadhar_passbook")
    if pattadhar_passbook_comment is not None:
        update_data["pattadhar_passbook_comment"] = pattadhar_passbook_comment

    if link_documents_file:
        update_data["link_documents_file"] = utils.save_files(
            link_documents_file, "link_documents")
    if link_documents_comment is not None:
        update_data["link_documents_comment"] = link_documents_comment

    if kasara_pahani_file:
        update_data["kasara_pahani_file"] = utils.save_files(
            kasara_pahani_file, "kasara_pahani")
    if kasara_pahani_comment is not None:
        update_data["kasara_pahani_comment"] = kasara_pahani_comment

    if encumbrance_certificate_file:
        update_data["encumbrance_certificate_file"] = utils.save_files(
            encumbrance_certificate_file, "encumbrance_certificate")
    if encumbrance_comment is not None:
        update_data["encumbrance_comment"] = encumbrance_comment

    if revenue_record_file:
        update_data["revenue_record_file"] = utils.save_files(
            revenue_record_file, "revenue_record")
    if revenue_record_comment is not None:
        update_data["revenue_record_comment"] = revenue_record_comment

    if partition_deed_file:
        update_data["partition_deed_file"] = utils.save_files(
            partition_deed_file, "partition_deed")
    if partition_comment is not None:
        update_data["partition_comment"] = partition_comment

    if faisal_patti_file:
        update_data["faisal_patti_file"] = utils.save_files(
            faisal_patti_file, "faisal_patti")
    if faisal_patti_comment is not None:
        update_data["faisal_patti_comment"] = faisal_patti_comment

    if death_certificate_file:
        update_data["death_certificate_file"] = utils.save_files(
            death_certificate_file, "death_certificate")
    if death_certificate_comment is not None:
        update_data["death_certificate_comment"] = death_certificate_comment

    if lease_agreement_file:
        update_data["lease_agreement_file"] = utils.save_files(
            lease_agreement_file, "lease_agreement")
    if lease_agreement_comment is not None:
        update_data["lease_agreement_comment"] = lease_agreement_comment

    if legal_opinion_report_file:
        update_data["legal_opinion_report_file"] = utils.save_files(
            legal_opinion_report_file, "legal_opinion_report")
    if legal_opinion_comment is not None:
        update_data["legal_opinion_comment"] = legal_opinion_comment

    if land_coordinates_file:
        update_data["land_coordinates_file"] = utils.save_files(
            land_coordinates_file, "land_coordinates")
    if land_coordinates_comment_file is not None:
        update_data["land_coordinates_comment_file"] = land_coordinates_comment_file

    if owner_kyc_video_file:
        update_data["owner_kyc_video_file"] = utils.save_files(
            owner_kyc_video_file, "owner_kyc_video")
    if owner_kyc_video_comment is not None:
        update_data["owner_kyc_video_comment"] = owner_kyc_video_comment

    legality_update = schemas.LegalityUpdate(**update_data)

    result = crud.update_legality(
        db=db, legality_id=legality_id, legality_data=legality_update)

    if result is None:
        return JSONResponse(status_code=404, content={"message": "Legality record not found"})

    logger.info(f"Legality record with ID {legality_id} updated successfully")
    return {"status_code": 200, "message": "Legality updated successfully", "data": result}


@app.post("/create-family-tree/", response_model=schemas.FamilyTreeResponse)
async def create_family_tree_endpoint(family_tree: schemas.FamilyTreeCreate, db: Session = Depends(get_db)):
    try:
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
        raise HTTPException(status_code=500, detail="An error occurred while retrieving FamilyTree records")


@app.put("/update-family-tree/{id}/", response_model=ApiResponse)
async def update_family_tree_endpoint(
    id: int,
    family_tree: schemas.FamilyTreeCreate,
    db: Session = Depends(get_db)
):
    try:
        db_family_tree = crud.update_family_tree(db=db, family_tree_id=id, family_tree=family_tree)

        response = ApiResponse(
            status_code=200,
            message="Family tree updated successfully",
            data={
                "id": db_family_tree.id,
                "father_name": db_family_tree.father_name,
                "father_age": db_family_tree.father_age,
                "mother_name": db_family_tree.mother_name,
                "mother_age": db_family_tree.mother_age,
                "owner_name": db_family_tree.owner_name,
                "owner_age": db_family_tree.owner_age,
                "religion": db_family_tree.religion,
                "num_wifes": db_family_tree.num_wifes,
                "num_kids": db_family_tree.num_kids,
                "num_siblings": db_family_tree.num_siblings
            }
        )
        return response
    except HTTPException as e:
        raise e
    except Exception as e:
        logger.error(f"Error in update_family_tree endpoint: {e}")
        raise HTTPException(status_code=500, detail="An error occurred while updating the FamilyTree")


@app.post("/create_land_boundaries/")
async def create_land_boundaries(
    land_images_file: List[UploadFile] = File(...),
    land_images_comments: Optional[str] = Form(None),
    landscape_view_of_farmland_file: List[UploadFile] = File(...),
    slope_side: Optional[str] = Form(None),
    slope_side_comments: Optional[str] = Form(None),
    shape_of_land: Optional[str] = Form(None),
    shape_of_land_comment: Optional[str] = Form(None),
    water_and_electricity_facility: Optional[str] = Form(None),
    water_facility: Optional[str] = Form(None),
    electricity_facility: Optional[str] = Form(None),
    water_and_electricity_facility_comments: Optional[str] = Form(None),
    masterplan_file: List[UploadFile] = File(...),
    masterplan_comments: Optional[str] = Form(None),
    east_boundaries_select: Optional[str] = Form(None),
    east_owner_name: Optional[str] = Form(None),
    east_age: Optional[int] = Form(None),
    east_boundaries_comments: Optional[str] = Form(None),
    west_boundaries_select: Optional[str] = Form(None),
    type_of_road: Optional[str] = Form(None),
    width_of_road: Optional[float] = Form(None),
    west_boundaries_comments: Optional[str] = Form(None),
    north_boundaries_select: Optional[str] = Form(None),
    tree_count: Optional[int] = Form(None),
    north_boundaries_comments: Optional[str] = Form(None),
    south_boundaries_select: Optional[str] = Form(None),
    south_boundaries_comments: Optional[str] = Form(None),
    survey_report: Optional[str] = Form(None),
    private_survey_file: List[UploadFile] = File(...),
    private_survey_number: Optional[str] = Form(None),
    government_survey_file: List[UploadFile] = File(...),
    government_survey_number: Optional[str] = Form(None),
    survey_report_comments: Optional[str] = Form(None),
    db: Session = Depends(get_db)
):
    try:
        logger.info("Started processing create_land_boundaries request")

        land_images_filenames = utils.save_files(land_images_file, "land_images")
        landscape_view_of_farmland_filenames = utils.save_files(landscape_view_of_farmland_file, "landscape_view_of_farmland")
        masterplan_filenames = utils.save_files(masterplan_file, "masterplan")
        private_survey_filenames = utils.save_files(private_survey_file, "private_survey")
        government_survey_filenames = utils.save_files(government_survey_file, "government_survey")

        land_boundaries_data = schemas.LandBoundariesCreate(
            land_images_file=land_images_filenames,
            land_images_comments=land_images_comments,
            landscape_view_of_farmland_file=landscape_view_of_farmland_filenames,
            slope_side=slope_side,
            slope_side_comments=slope_side_comments,
            shape_of_land=shape_of_land,
            shape_of_land_comment=shape_of_land_comment,
            water_and_electricity_facility=water_and_electricity_facility,
            water_facility=water_facility,
            electricity_facility=electricity_facility,
            water_and_electricity_facility_comments=water_and_electricity_facility_comments,
            masterplan_file=masterplan_filenames,
            masterplan_comments=masterplan_comments,
            east_boundaries_select=east_boundaries_select,
            east_owner_name=east_owner_name,
            east_age=east_age,
            east_boundaries_comments=east_boundaries_comments,
            west_boundaries_select=west_boundaries_select,
            type_of_road=type_of_road,
            width_of_road=width_of_road,
            west_boundaries_comments=west_boundaries_comments,
            north_boundaries_select=north_boundaries_select,
            tree_count=tree_count,
            north_boundaries_comments=north_boundaries_comments,
            south_boundaries_select=south_boundaries_select,
            south_boundaries_comments=south_boundaries_comments,
            survey_report=survey_report,
            private_survey_file=private_survey_filenames,
            private_survey_number=private_survey_number,
            government_survey_file=government_survey_filenames,
            government_survey_number=government_survey_number,
            survey_report_comments=survey_report_comments,
        )

        logger.info("Prepared land boundaries data for database insertion")
        result = crud.create_land_boundaries(db=db, land_boundaries=land_boundaries_data)
        logger.info(f"Land Boundaries record created with ID {result.id}")

        response_data = {
            "status_code": 201,
            "message": "Land Boundaries created successfully",
            "data": {
                "id": result.id,
                "land_images_file": result.land_images_file,
                "land_images_comments": result.land_images_comments,
                "landscape_view_of_farmland_file": result.landscape_view_of_farmland_file,
                "slope_side": result.slope_side,
                "slope_side_comments": result.slope_side_comments,
                "shape_of_land": result.shape_of_land,
                "shape_of_land_comment": result.shape_of_land_comment,
                "water_and_electricity_facility": result.water_and_electricity_facility,
                "water_facility": result.water_facility,
                "electricity_facility": result.electricity_facility,
                "water_and_electricity_facility_comments": result.water_and_electricity_facility_comments,
                "masterplan_file": result.masterplan_file,
                "masterplan_comments": result.masterplan_comments,
                "east_boundaries_select": result.east_boundaries_select,
                "east_owner_name": result.east_owner_name,
                "east_age": result.east_age,
                "east_boundaries_comments": result.east_boundaries_comments,
                "west_boundaries_select": result.west_boundaries_select,
                "type_of_road": result.type_of_road,
                "width_of_road": result.width_of_road,
                "west_boundaries_comments": result.west_boundaries_comments,
                "north_boundaries_select": result.north_boundaries_select,
                "tree_count": result.tree_count,
                "north_boundaries_comments": result.north_boundaries_comments,
                "south_boundaries_select": result.south_boundaries_select,
                "south_boundaries_comments": result.south_boundaries_comments,
                "survey_report": result.survey_report,
                "private_survey_file": result.private_survey_file,
                "private_survey_number": result.private_survey_number,
                "government_survey_file": result.government_survey_file,
                "government_survey_number": result.government_survey_number,
                "survey_report_comments": result.survey_report_comments,
            }
        }

        return response_data
    except Exception as e:
        logger.error(f"Error processing create_land_boundaries request: {e}")
        return {
            "status_code": 500,
            "message": "Failed to create land boundaries",
            "error": str(e)
        }


@app.get("/List_land_boundaries/", response_model=schemas.LandBoundariesListResponse)
async def get_land_boundaries_list(db: Session = Depends(get_db)):
    try:
        land_boundaries_records = db.query(models.LandBoundaries).all()

        if not land_boundaries_records:
            raise HTTPException(status_code=404, detail="No land boundaries records found")

        land_boundaries_response = [schemas.LandBoundariesResponse.from_orm(record) for record in land_boundaries_records]

        return schemas.LandBoundariesListResponse(land_boundaries=land_boundaries_response)
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"An unexpected error occurred: {str(e)}")


@app.put("/update_land_boundaries/{land_id}/")
async def update_land_boundaries_api(
    land_id: int,
    land_images_file: List[UploadFile] = File(...),
    land_images_comments: str = Form(...),
    landscape_view_of_farmland_file: List[UploadFile] = File(...),
    slope_side: str = Form(...),
    slope_side_comments: str = Form(...),
    shape_of_land: str = Form(...),
    shape_of_land_comment: str = Form(...),
    water_and_electricity_facility: str = Form(...),
    water_facility: str = Form(...),
    electricity_facility: str = Form(...),
    water_and_electricity_facility_comments: str = Form(...),
    masterplan_file: List[UploadFile] = File(...),
    masterplan_comments: str = Form(...),
    east_boundaries_select: str = Form(...),
    east_owner_name: str = Form(...),
    east_age: int = Form(...),
    east_boundaries_comments: str = Form(...),
    west_boundaries_select: str = Form(...),
    type_of_road: str = Form(...),
    width_of_road: float = Form(...),
    west_boundaries_comments: str = Form(...),
    north_boundaries_select: str = Form(...),
    tree_count: int = Form(...),
    north_boundaries_comments: str = Form(...),
    south_boundaries_select: str = Form(...),
    south_boundaries_comments: str = Form(...),
    survey_report: str = Form(...),
    private_survey_file: List[UploadFile] = File(...),
    private_survey_number: str = Form(...),
    government_survey_file: List[UploadFile] = File(...),
    government_survey_number: str = Form(...),
    survey_report_comments: str = Form(...),
    db: Session = Depends(get_db)
):
    try:
       
        land_images_file_paths = utils.save_files(land_images_file, "land_images")
        landscape_view_file_paths = utils.save_files(landscape_view_of_farmland_file, "landscape_view")
        masterplan_file_paths = utils.save_files(masterplan_file, "masterplans")
        private_survey_file_paths = utils.save_files(private_survey_file, "private_survey")
        government_survey_file_paths = utils.save_files(government_survey_file, "government_survey")

        form_data = schemas.LandBoundariesUpdate(
            land_images_file=land_images_file_paths,
            land_images_comments=land_images_comments,
            landscape_view_of_farmland_file=landscape_view_file_paths,
            slope_side=slope_side,
            slope_side_comments=slope_side_comments,
            shape_of_land=shape_of_land,
            shape_of_land_comment=shape_of_land_comment,
            water_and_electricity_facility=water_and_electricity_facility,
            water_facility=water_facility,
            electricity_facility=electricity_facility,
            water_and_electricity_facility_comments=water_and_electricity_facility_comments,
            masterplan_file=masterplan_file_paths,
            masterplan_comments=masterplan_comments,
            east_boundaries_select=east_boundaries_select,
            east_owner_name=east_owner_name,
            east_age=east_age,
            east_boundaries_comments=east_boundaries_comments,
            west_boundaries_select=west_boundaries_select,
            type_of_road=type_of_road,
            width_of_road=width_of_road,
            west_boundaries_comments=west_boundaries_comments,
            north_boundaries_select=north_boundaries_select,
            tree_count=tree_count,
            north_boundaries_comments=north_boundaries_comments,
            south_boundaries_select=south_boundaries_select,
            south_boundaries_comments=south_boundaries_comments,
            survey_report=survey_report,
            private_survey_file=private_survey_file_paths,
            private_survey_number=private_survey_number,
            government_survey_file=government_survey_file_paths,
            government_survey_number=government_survey_number,
            survey_report_comments=survey_report_comments
        )
        updated_land = crud.update_land_boundaries(db=db, land_id=land_id, data=form_data)

        if not updated_land:
            raise HTTPException(status_code=404, detail="Land not found")

        response_data = {
            "status_code": 200,
            "message": "Land Boundaries updated successfully",
            "data": {
                "id": updated_land.id,
                "land_images_file": updated_land.land_images_file,
                "land_images_comments": updated_land.land_images_comments,
                "landscape_view_of_farmland_file": updated_land.landscape_view_of_farmland_file,
                "slope_side": updated_land.slope_side,
                "slope_side_comments": updated_land.slope_side_comments,
                "shape_of_land": updated_land.shape_of_land,
                "shape_of_land_comment": updated_land.shape_of_land_comment,
                "water_and_electricity_facility": updated_land.water_and_electricity_facility,
                "water_facility": updated_land.water_facility,
                "electricity_facility": updated_land.electricity_facility,
                "water_and_electricity_facility_comments": updated_land.water_and_electricity_facility_comments,
                "masterplan_file": updated_land.masterplan_file,
                "masterplan_comments": updated_land.masterplan_comments,
                "east_boundaries_select": updated_land.east_boundaries_select,
                "east_owner_name": updated_land.east_owner_name,
                "east_age": updated_land.east_age,
                "east_boundaries_comments": updated_land.east_boundaries_comments,
                "west_boundaries_select": updated_land.west_boundaries_select,
                "type_of_road": updated_land.type_of_road,
                "width_of_road": updated_land.width_of_road,
                "west_boundaries_comments": updated_land.west_boundaries_comments,
                "north_boundaries_select": updated_land.north_boundaries_select,
                "tree_count": updated_land.tree_count,
                "north_boundaries_comments": updated_land.north_boundaries_comments,
                "south_boundaries_select": updated_land.south_boundaries_select,
                "south_boundaries_comments": updated_land.south_boundaries_comments,
                "survey_report": updated_land.survey_report,
                "private_survey_file": updated_land.private_survey_file,
                "private_survey_number": updated_land.private_survey_number,
                "government_survey_file": updated_land.government_survey_file,
                "government_survey_number": updated_land.government_survey_number,
                "survey_report_comments": updated_land.survey_report_comments,
            }
        }
        return response_data

    except Exception as e:
        logger.error(f"Error processing update_land_boundaries request: {e}")
        return {
            "status_code": 500,
            "message": "Failed to update land boundaries",
            "error": str(e)
        }


@app.post("/create_valuation/")
async def create_valuation(
    village_map_or_naksha_file: List[UploadFile] = File(...),
    village_map_or_naksha_comments: Optional[str] = Form(None),
    sub_register_value_file: List[UploadFile] = File(...),
    sub_register_value_comments: Optional[str] = Form(None),
    valuator_report_file: List[UploadFile] = File(...),
    valuator_report_comments: Optional[str] = Form(None),
    land_owner_value_file: List[UploadFile] = File(...),
    land_owner_value_comments: Optional[str] = Form(None),
    road_approach_type: Optional[str] = Form(None),
    road_width: Optional[float] = Form(None),
    road_approach_comments: Optional[str] = Form(None),
    water_facility: Optional[bool] = Form(None),
    primary_source_of_land: Optional[str] = Form(None),
    water_facility_comments: Optional[str] = Form(None),
    recent_transaction_in_surrounding: Optional[str] = Form(None),
    valuation_per_acre: Optional[float] = Form(None),
    local_market_acre_price: Optional[float] = Form(None),
    recent_transaction_comments: Optional[str] = Form(None),
    electricity_facility: Optional[bool] = Form(None),
    electricity_comments: Optional[str] = Form(None),
    existing_trees: Optional[bool] = Form(None),
    tree_count: Optional[int] = Form(None),
    trees_comments: Optional[str] = Form(None),
    surrounding_mines: Optional[bool] = Form(None),
    mines_comments: Optional[str] = Form(None),
    disadvantages_comments: Optional[str] = Form(None),
    future_plans_comments: Optional[str] = Form(None),
    upcoming_infrastructures: Optional[bool] = Form(None),
    infrastructures_list: Optional[str] = Form(None),
    infrastructures_comments: Optional[str] = Form(None),
    railway_connectivity: Optional[bool] = Form(None),
    railway_distance: Optional[float] = Form(None),
    railway_comments: Optional[str] = Form(None),
    airport_connectivity: Optional[bool] = Form(None),
    airport_distance: Optional[float] = Form(None),
    airport_comments: Optional[str] = Form(None),
    db: Session = Depends(get_db)
):
    try:
        logger.info("Started processing create_valuation request")

        village_map_or_naksha_filenames = utils.save_files(village_map_or_naksha_file, "village_map_or_naksha")
        sub_register_value_filenames = utils.save_files(sub_register_value_file, "sub_register_value")
        valuator_report_filenames = utils.save_files(valuator_report_file, "valuator_report")
        land_owner_value_filenames = utils.save_files(land_owner_value_file, "land_owner_value")

        valuation_data = schemas.ValuationCreate(
            village_map_or_naksha_file=village_map_or_naksha_filenames,
            village_map_or_naksha_comments=village_map_or_naksha_comments,
            sub_register_value_file=sub_register_value_filenames,
            sub_register_value_comments=sub_register_value_comments,
            valuator_report_file=valuator_report_filenames,
            valuator_report_comments=valuator_report_comments,
            land_owner_value_file=land_owner_value_filenames,
            land_owner_value_comments=land_owner_value_comments,
            road_approach_type=road_approach_type,
            road_width=road_width,
            road_approach_comments=road_approach_comments,
            water_facility=water_facility,
            primary_source_of_land=primary_source_of_land,
            water_facility_comments=water_facility_comments,
            recent_transaction_in_surrounding=recent_transaction_in_surrounding,
            valuation_per_acre=valuation_per_acre,
            local_market_acre_price=local_market_acre_price,
            recent_transaction_comments=recent_transaction_comments,
            electricity_facility=electricity_facility,
            electricity_comments=electricity_comments,
            existing_trees=existing_trees,
            tree_count=tree_count,
            trees_comments=trees_comments,
            surrounding_mines=surrounding_mines,
            mines_comments=mines_comments,
            disadvantages_comments=disadvantages_comments,
            future_plans_comments=future_plans_comments,
            upcoming_infrastructures=upcoming_infrastructures,
            infrastructures_list=infrastructures_list,
            infrastructures_comments=infrastructures_comments,
            railway_connectivity=railway_connectivity,
            railway_distance=railway_distance,
            railway_comments=railway_comments,
            airport_connectivity=airport_connectivity,
            airport_distance=airport_distance,
            airport_comments=airport_comments
        )

        logger.info("Prepared valuation data for database insertion")
        result = crud.create_valuation(db=db, valuation=valuation_data)
        logger.info(f"Valuation record created with ID {result.id}")

        response_data = {
            "status_code": 201,
            "message": "Valuation created successfully",
            "data": {
                "id": result.id,
                "village_map_or_naksha_file": result.village_map_or_naksha_file,
                "village_map_or_naksha_comments": result.village_map_or_naksha_comments,
                "sub_register_value_file": result.sub_register_value_file,
                "sub_register_value_comments": result.sub_register_value_comments,
                "valuator_report_file": result.valuator_report_file,
                "valuator_report_comments": result.valuator_report_comments,
                "land_owner_value_file": result.land_owner_value_file,
                "land_owner_value_comments": result.land_owner_value_comments,
                "road_approach_type": result.road_approach_type,
                "road_width": result.road_width,
                "road_approach_comments": result.road_approach_comments,
                "water_facility": result.water_facility,
                "primary_source_of_land": result.primary_source_of_land,
                "water_facility_comments": result.water_facility_comments,
                "recent_transaction_in_surrounding": result.recent_transaction_in_surrounding,
                "valuation_per_acre": result.valuation_per_acre,
                "local_market_acre_price": result.local_market_acre_price,
                "recent_transaction_comments": result.recent_transaction_comments,
                "electricity_facility": result.electricity_facility,
                "electricity_comments": result.electricity_comments,
                "existing_trees": result.existing_trees,
                "tree_count": result.tree_count,
                "trees_comments": result.trees_comments,
                "surrounding_mines": result.surrounding_mines,
                "mines_comments": result.mines_comments,
                "disadvantages_comments": result.disadvantages_comments,
                "future_plans_comments": result.future_plans_comments,
                "upcoming_infrastructures": result.upcoming_infrastructures,
                "infrastructures_list": result.infrastructures_list,
                "infrastructures_comments": result.infrastructures_comments,
                "railway_connectivity": result.railway_connectivity,
                "railway_distance": result.railway_distance,
                "railway_comments": result.railway_comments,
                "airport_connectivity": result.airport_connectivity,
                "airport_distance": result.airport_distance,
                "airport_comments": result.airport_comments,
            }
        }
        return response_data
    except Exception as e:
        logger.error(f"Error processing create_valuation request: {e}")
        return {
            "status_code": 500,
            "message": "Failed to create valuation",
            "error": str(e)
        }


@app.get("/list_valuations/", response_model=ValuationListResponse)
async def get_valuation_list(db: Session = Depends(get_db)):
    try:
        valuation_records = db.query(models.Valuation).all()
        if not valuation_records:
            raise HTTPException(status_code=404, detail="No valuation records found")
        valuation_response = [
            ValuationResponse.from_orm(record) for record in valuation_records
        ]
        return ValuationListResponse(valuations=valuation_response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {str(e)}")


@app.put("/update_valuation/{valuation_id}/")
async def update_valuation_api(
    valuation_id: int,
    village_map_or_naksha_files: List[UploadFile] = File(...),
    village_map_or_naksha_comments: str = Form(...),
    sub_register_value_files: List[UploadFile] = File(...),
    sub_register_value_comments: str = Form(...),
    valuator_report_files: List[UploadFile] = File(...),
    valuator_report_comments: str = Form(...),
    land_owner_value_files: List[UploadFile] = File(...),
    land_owner_value_comments: str = Form(...),
    road_approach_type: str = Form(...),
    road_width: float = Form(...),
    road_approach_comments: str = Form(...),
    water_facility: bool = Form(...),
    primary_source_of_land: str = Form(...),
    water_facility_comments: str = Form(...),
    recent_transaction_in_surrounding: str = Form(...),
    valuation_per_acre: float = Form(...),
    local_market_acre_price: float = Form(...),
    recent_transaction_comments: str = Form(...),
    electricity_facility: bool = Form(...),
    electricity_comments: str = Form(...),
    existing_trees: bool = Form(...),
    tree_count: int = Form(...),
    trees_comments: str = Form(...),
    surrounding_mines: bool = Form(...),
    mines_comments: str = Form(...),
    disadvantages_comments: str = Form(...),
    future_plans_comments: str = Form(...),
    upcoming_infrastructures: bool = Form(...),
    infrastructures_list: str = Form(...),
    infrastructures_comments: str = Form(...),
    railway_connectivity: bool = Form(...),
    railway_distance: float = Form(...),
    railway_comments: str = Form(...),
    airport_connectivity: bool = Form(...),
    airport_distance: float = Form(...),
    airport_comments: str = Form(...),
    db: Session = Depends(get_db)
):
    try:
        village_map_or_naksha_file_paths = utils.save_files(
            village_map_or_naksha_files, "village_map_or_naksha")
        sub_register_value_file_paths = utils.save_files(
            sub_register_value_files, "sub_register_value")
        valuator_report_file_paths = utils.save_files(
            valuator_report_files, "valuator_report")
        land_owner_value_file_paths = utils.save_files(
            land_owner_value_files, "land_owner_value")

        form_data = schemas.ValuationUpdate(
            village_map_or_naksha_file=village_map_or_naksha_file_paths,
            village_map_or_naksha_comments=village_map_or_naksha_comments,
            sub_register_value_file=sub_register_value_file_paths,
            sub_register_value_comments=sub_register_value_comments,
            valuator_report_file=valuator_report_file_paths,
            valuator_report_comments=valuator_report_comments,
            land_owner_value_file=land_owner_value_file_paths,
            land_owner_value_comments=land_owner_value_comments,
            road_approach_type=road_approach_type,
            road_width=road_width,
            road_approach_comments=road_approach_comments,
            water_facility=water_facility,
            primary_source_of_land=primary_source_of_land,
            water_facility_comments=water_facility_comments,
            recent_transaction_in_surrounding=recent_transaction_in_surrounding,
            valuation_per_acre=valuation_per_acre,
            local_market_acre_price=local_market_acre_price,
            recent_transaction_comments=recent_transaction_comments,
            electricity_facility=electricity_facility,
            electricity_comments=electricity_comments,
            existing_trees=existing_trees,
            tree_count=tree_count,
            trees_comments=trees_comments,
            surrounding_mines=surrounding_mines,
            mines_comments=mines_comments,
            disadvantages_comments=disadvantages_comments,
            future_plans_comments=future_plans_comments,
            upcoming_infrastructures=upcoming_infrastructures,
            infrastructures_list=infrastructures_list,
            infrastructures_comments=infrastructures_comments,
            railway_connectivity=railway_connectivity,
            railway_distance=railway_distance,
            railway_comments=railway_comments,
            airport_connectivity=airport_connectivity,
            airport_distance=airport_distance,
            airport_comments=airport_comments,
        )

        updated_valuation = crud.update_valuation(db, valuation_id, form_data)

        if not updated_valuation:
            raise HTTPException(status_code=404, detail="Valuation not found")

        response_data = {
            "status_code": 200,
            "message": "Valuation updated successfully",
            "data": {
                "id": updated_valuation.id,
                "village_map_or_naksha_file": updated_valuation.village_map_or_naksha_file,
                "village_map_or_naksha_comments": updated_valuation.village_map_or_naksha_comments,
                "sub_register_value_file": updated_valuation.sub_register_value_file,
                "sub_register_value_comments": updated_valuation.sub_register_value_comments,
                "valuator_report_file": updated_valuation.valuator_report_file,
                "valuator_report_comments": updated_valuation.valuator_report_comments,
                "land_owner_value_file": updated_valuation.land_owner_value_file,
                "land_owner_value_comments": updated_valuation.land_owner_value_comments,
                "road_approach_type": updated_valuation.road_approach_type,
                "road_width": updated_valuation.road_width,
                "road_approach_comments": updated_valuation.road_approach_comments,
                "water_facility": updated_valuation.water_facility,
                "primary_source_of_land": updated_valuation.primary_source_of_land,
                "water_facility_comments": updated_valuation.water_facility_comments,
                "recent_transaction_in_surrounding": updated_valuation.recent_transaction_in_surrounding,
                "valuation_per_acre": updated_valuation.valuation_per_acre,
                "local_market_acre_price": updated_valuation.local_market_acre_price,
                "recent_transaction_comments": updated_valuation.recent_transaction_comments,
                "electricity_facility": updated_valuation.electricity_facility,
                "electricity_comments": updated_valuation.electricity_comments,
                "existing_trees": updated_valuation.existing_trees,
                "tree_count": updated_valuation.tree_count,
                "trees_comments": updated_valuation.trees_comments,
                "surrounding_mines": updated_valuation.surrounding_mines,
                "mines_comments": updated_valuation.mines_comments,
                "disadvantages_comments": updated_valuation.disadvantages_comments,
                "future_plans_comments": updated_valuation.future_plans_comments,
                "upcoming_infrastructures": updated_valuation.upcoming_infrastructures,
                "infrastructures_list": updated_valuation.infrastructures_list,
                "infrastructures_comments": updated_valuation.infrastructures_comments,
                "railway_connectivity": updated_valuation.railway_connectivity,
                "railway_distance": updated_valuation.railway_distance,
                "railway_comments": updated_valuation.railway_comments,
                "airport_connectivity": updated_valuation.airport_connectivity,
                "airport_distance": updated_valuation.airport_distance,
                "airport_comments": updated_valuation.airport_comments,
            }
        }

        return response_data

    except Exception as e:
        logger.error(f"Error processing update_valuation request: {e}")
        return {
            "status_code": 500,
            "message": "Failed to update valuation",
            "error": str(e)
        }


@app.post("/create_agriculture_certification/")
async def create_agriculture_certification(
    local_agriculture_officer_report_file: List[UploadFile] = File(...),
    local_agriculture_officer_report_comments: Optional[str] = Form(None),
    last_5_years_crop_yielding_report_file: List[UploadFile] = File(...),
    last_5_years_crop_yielding_report_comments: Optional[str] = Form(None),
    soil=Form(None),
    soil_comments=Form(None),
    types_of_crop=Form(None),
    types_of_crop_comments=Form(None),
    types_of_crop_can_be_grown=Form(None),
    types_of_crop_can_be_grown_comments=Form(None),
    ground_water_level=Form(None),
    ground_water_level_comments=Form(None),
    current_yielding_cost=Form(None),
    current_returns_from_yield=Form(None),
    current_yielding_cost_comments=Form(None),
    current_cultivation=Form(None),
    current_cultivation_name=Form(None),
    current_cultivation_contact_details=Form(None),
    current_cultivation_comments=Form(None),
    natural_advantages_disadvantages_comments=Form(None),
    future_crop_plans_comments=Form(None),
    suggested_crop_by_green_land=Form(None),
    best_returns=Form(None),
    suggested_crop_comments=Form(None),
    db: Session = Depends(get_db)
):
    try:
        logger.info(
            "Started processing create_agriculture_certification request")

        local_agriculture_officer_report_file = utils.save_files(
            local_agriculture_officer_report_file, "local_agriculture_officer_report_file")
        last_5_years_crop_yielding_report_file = utils.save_files(
            last_5_years_crop_yielding_report_file, "last_5_years_crop_yielding_report_file")

        agriculture_certification = schemas.AgricultureCertificationCreate(
            local_agriculture_officer_report_file=local_agriculture_officer_report_file,
            local_agriculture_officer_report_comments=local_agriculture_officer_report_comments,
            last_5_years_crop_yielding_report_file=last_5_years_crop_yielding_report_file,
            last_5_years_crop_yielding_report_comments=last_5_years_crop_yielding_report_comments,
            soil=soil,
            soil_comments=soil_comments,
            types_of_crop=types_of_crop,
            types_of_crop_comments=types_of_crop_comments,
            types_of_crop_can_be_grown=types_of_crop_can_be_grown,
            types_of_crop_can_be_grown_comments=types_of_crop_can_be_grown_comments,
            ground_water_level=ground_water_level,
            ground_water_level_comments=ground_water_level_comments,
            current_yielding_cost=current_yielding_cost,
            current_returns_from_yield=current_returns_from_yield,
            current_yielding_cost_comments=current_yielding_cost_comments,
            current_cultivation=current_cultivation,
            current_cultivation_name=current_cultivation_name,
            current_cultivation_contact_details=current_cultivation_contact_details,
            current_cultivation_comments=current_cultivation_comments,
            natural_advantages_disadvantages_comments=natural_advantages_disadvantages_comments,
            future_crop_plans_comments=future_crop_plans_comments,
            suggested_crop_by_green_land=suggested_crop_by_green_land,
            best_returns=best_returns,
            suggested_crop_comments=suggested_crop_comments
        )

        new_agriculture_certification = crud.create_agriculture_certification(
            db=db, certification_data=agriculture_certification
        )

        response_data = {
            "status_code": 201,
            "message": "Agriculture certification created successfully",
            "data": {
                "id": new_agriculture_certification.id,
                "local_agriculture_officer_report_file": new_agriculture_certification.local_agriculture_officer_report_file,
                "local_agriculture_officer_report_comments": new_agriculture_certification.local_agriculture_officer_report_comments,
                "last_5_years_crop_yielding_report_file": new_agriculture_certification.last_5_years_crop_yielding_report_file,
                "last_5_years_crop_yielding_report_comments": new_agriculture_certification.last_5_years_crop_yielding_report_comments,
                "soil": new_agriculture_certification.soil,
                "soil_comments": new_agriculture_certification.soil_comments,
                "types_of_crop": new_agriculture_certification.types_of_crop,
                "types_of_crop_comments": new_agriculture_certification.types_of_crop_comments,
                "types_of_crop_can_be_grown": new_agriculture_certification.types_of_crop_can_be_grown,
                "types_of_crop_can_be_grown_comments": new_agriculture_certification.types_of_crop_can_be_grown_comments,
                "ground_water_level": new_agriculture_certification.ground_water_level,
                "ground_water_level_comments": new_agriculture_certification.ground_water_level_comments,
                "current_yielding_cost": new_agriculture_certification.current_yielding_cost,
                "current_returns_from_yield": new_agriculture_certification.current_returns_from_yield,
                "current_yielding_cost_comments": new_agriculture_certification.current_yielding_cost_comments,
                "current_cultivation": new_agriculture_certification.current_cultivation,
                "current_cultivation_name": new_agriculture_certification.current_cultivation_name,
                "current_cultivation_contact_details": new_agriculture_certification.current_cultivation_contact_details,
                "current_cultivation_comments": new_agriculture_certification.current_cultivation_comments,
                "natural_advantages_disadvantages_comments": new_agriculture_certification.natural_advantages_disadvantages_comments,
                "future_crop_plans_comments": new_agriculture_certification.future_crop_plans_comments,
                "suggested_crop_by_green_land": new_agriculture_certification.suggested_crop_by_green_land,
                "best_returns": new_agriculture_certification.best_returns,
                "suggested_crop_comments": new_agriculture_certification.suggested_crop_comments
            }
        }

        logger.info("Agriculture certification created successfully")
        return response_data
    except Exception as e:
        logger.error(
            f"Error processing create_agriculture_certification request: {e}")
        return {
            "status_code": 500,
            "message": "Failed to create agriculture certification",
            "error": str(e)
        }

@app.get("/list_agriculture_certifications/", response_model=schemas.AgricultureCertificationListResponse)
async def list_agriculture_certifications(db: Session = Depends(get_db)):
    agriculture_records = db.query(models.AgricultureCertification).all()
    if not agriculture_records:
        raise HTTPException(status_code=404, detail="No agriculture certification records found")
    agriculture_response = [schemas.AgricultureCertificationResponse.from_orm(
        record) for record in agriculture_records]
    return {"agriculture_certifications": agriculture_response}

@app.put("/update_agriculture_certification/{agriculture_certification_id}/")
async def update_agriculture_certification_api(
    agriculture_certification_id: int,
    local_agriculture_officer_report_file: List[UploadFile] = File(...),
    local_agriculture_officer_report_comments: str = Form(...),
    last_5_years_crop_yielding_report_file: List[UploadFile] = File(...),
    last_5_years_crop_yielding_report_comments: str = Form(...),
    soil: str = Form(...),
    soil_comments: str = Form(...),
    types_of_crop: str = Form(...),
    types_of_crop_comments: str = Form(...),
    types_of_crop_can_be_grown: str = Form(...),
    types_of_crop_can_be_grown_comments: str = Form(...),
    ground_water_level: str = Form(...),
    ground_water_level_comments: str = Form(...),
    current_yielding_cost: int = Form(...),
    current_returns_from_yield: int = Form(...),
    current_yielding_cost_comments: str = Form(...),
    current_cultivation: str = Form(...),
    current_cultivation_name: str = Form(...),
    current_cultivation_contact_details: str = Form(...),
    current_cultivation_comments: str = Form(...),
    natural_advantages_disadvantages_comments: str = Form(...),
    future_crop_plans_comments: str = Form(...),
    suggested_crop_by_green_land: str = Form(...),
    best_returns: int = Form(...),
    suggested_crop_comments: str = Form(...),
    db: Session = Depends(get_db)
):
    try:
        local_agriculture_officer_report_file_paths = utils.save_files(
            local_agriculture_officer_report_file, "agriculture_certification"
        )
        last_5_years_crop_yielding_report_file_paths = utils.save_files(
            last_5_years_crop_yielding_report_file, "agriculture_certification"
        )

        form_data = schemas.AgricultureCertificationUpdate(
            local_agriculture_officer_report_file=local_agriculture_officer_report_file_paths,
            local_agriculture_officer_report_comments=local_agriculture_officer_report_comments,
            last_5_years_crop_yielding_report_file=last_5_years_crop_yielding_report_file_paths,
            last_5_years_crop_yielding_report_comments=last_5_years_crop_yielding_report_comments,
            soil=soil,
            soil_comments=soil_comments,
            types_of_crop=types_of_crop,
            types_of_crop_comments=types_of_crop_comments,
            types_of_crop_can_be_grown=types_of_crop_can_be_grown,
            types_of_crop_can_be_grown_comments=types_of_crop_can_be_grown_comments,
            ground_water_level=ground_water_level,
            ground_water_level_comments=ground_water_level_comments,
            current_yielding_cost=current_yielding_cost,
            current_returns_from_yield=current_returns_from_yield,
            current_yielding_cost_comments=current_yielding_cost_comments,
            current_cultivation=current_cultivation,
            current_cultivation_name=current_cultivation_name,
            current_cultivation_contact_details=current_cultivation_contact_details,
            current_cultivation_comments=current_cultivation_comments,
            natural_advantages_disadvantages_comments=natural_advantages_disadvantages_comments,
            future_crop_plans_comments=future_crop_plans_comments,
            suggested_crop_by_green_land=suggested_crop_by_green_land,
            best_returns=best_returns,
            suggested_crop_comments=suggested_crop_comments,
        )

        updated_certification = crud.update_agriculture_certification(
            db, agriculture_certification_id, form_data
        )

        if updated_certification:
            response_data = {
                "status_code": 200,
                "message": "Agriculture certification updated successfully",
                "data": {
                    "id": updated_certification.id,
                    "local_agriculture_officer_report_file": updated_certification.local_agriculture_officer_report_file,
                    "local_agriculture_officer_report_comments": updated_certification.local_agriculture_officer_report_comments,
                    "last_5_years_crop_yielding_report_file": updated_certification.last_5_years_crop_yielding_report_file,
                    "last_5_years_crop_yielding_report_comments": updated_certification.last_5_years_crop_yielding_report_comments,
                    "soil": updated_certification.soil,
                    "soil_comments": updated_certification.soil_comments,
                    "types_of_crop": updated_certification.types_of_crop,
                    "types_of_crop_comments": updated_certification.types_of_crop_comments,
                    "types_of_crop_can_be_grown": updated_certification.types_of_crop_can_be_grown,
                    "types_of_crop_can_be_grown_comments": updated_certification.types_of_crop_can_be_grown_comments,
                    "ground_water_level": updated_certification.ground_water_level,
                    "ground_water_level_comments": updated_certification.ground_water_level_comments,
                    "current_yielding_cost": updated_certification.current_yielding_cost,
                    "current_returns_from_yield": updated_certification.current_returns_from_yield,
                    "current_yielding_cost_comments": updated_certification.current_yielding_cost_comments,
                    "current_cultivation": updated_certification.current_cultivation,
                    "current_cultivation_name": updated_certification.current_cultivation_name,
                    "current_cultivation_contact_details": updated_certification.current_cultivation_contact_details,
                    "current_cultivation_comments": updated_certification.current_cultivation_comments,
                    "natural_advantages_disadvantages_comments": updated_certification.natural_advantages_disadvantages_comments,
                    "future_crop_plans_comments": updated_certification.future_crop_plans_comments,
                    "suggested_crop_by_green_land": updated_certification.suggested_crop_by_green_land,
                    "best_returns": updated_certification.best_returns,
                    "suggested_crop_comments": updated_certification.suggested_crop_comments
                }
            }
            logger.info("Agriculture certification updated successfully")
            return response_data
        else:
            raise HTTPException(
                status_code=404, detail="Agriculture Certification not found"
            )
    except Exception as e:
        logger.error(
            f"Error processing update_agriculture_certification request: {e}")
        raise HTTPException(status_code=500, detail=f"An error occurred: {e}")



@app.post("/create_local_intelligence/")
async def create_local_intelligence(
    issues_with_boundaries_and_owners: Optional[str] = Form(None),
    issues_with_boundaries_and_owners_comments: Optional[str] = Form(None),
    local_liabilities: Optional[str] = Form(None),
    local_liabilities_comments: Optional[str] = Form(None),
    bank_loans_or_pending_loans: Optional[str] = Form(None),
    loan_amount: Optional[int] = Form(None),
    bank_loans_or_pending_loans_comments: Optional[str] = Form(None),
    owner_mindset: Optional[str] = Form(None),
    owner_mindset_comments: Optional[str] = Form(None),
    source_person: Optional[str] = Form(None),
    source_person_name: Optional[str] = Form(None),
    source_person_contact_details: Optional[str] = Form(None),
    source_person_comments: Optional[str] = Form(None),
    paper_agreement: Optional[str] = Form(None),
    agreement_type: Optional[str] = Form(None),
    last_price_of_land: Optional[int] = Form(None),
    paper_agreement_comments: Optional[str] = Form(None),
    previous_transactions_on_land: Optional[str] = Form(None),
    previous_transaction_amount: Optional[int] = Form(None),
    previous_transaction_comments: Optional[str] = Form(None),
    db: Session = Depends(get_db)
):
    try:
        logger.info("Started processing create_local_intelligence request")

        local_intelligence = schemas.LocalIntelligenceCreate(
            issues_with_boundaries_and_owners=issues_with_boundaries_and_owners,
            issues_with_boundaries_and_owners_comments=issues_with_boundaries_and_owners_comments,
            local_liabilities=local_liabilities,
            local_liabilities_comments=local_liabilities_comments,
            bank_loans_or_pending_loans=bank_loans_or_pending_loans,
            loan_amount=loan_amount,
            bank_loans_or_pending_loans_comments=bank_loans_or_pending_loans_comments,
            owner_mindset=owner_mindset,
            owner_mindset_comments=owner_mindset_comments,
            source_person=source_person,
            source_person_name=source_person_name,
            source_person_contact_details=source_person_contact_details,
            source_person_comments=source_person_comments,
            paper_agreement=paper_agreement,
            agreement_type=agreement_type,
            last_price_of_land=last_price_of_land,
            paper_agreement_comments=paper_agreement_comments,
            previous_transactions_on_land=previous_transactions_on_land,
            previous_transaction_amount=previous_transaction_amount,
            previous_transaction_comments=previous_transaction_comments
        )

        new_local_intelligence = crud.create_local_intelligence(
            db=db, intelligence_data=local_intelligence
        )

        response_data = {
            "status_code": 201,
            "message": "Local intelligence created successfully",
            "data": {
                "id": new_local_intelligence.id,
                "issues_with_boundaries_and_owners": new_local_intelligence.issues_with_boundaries_and_owners,
                "issues_with_boundaries_and_owners_comments": new_local_intelligence.issues_with_boundaries_and_owners_comments,
                "local_liabilities": new_local_intelligence.local_liabilities,
                "local_liabilities_comments": new_local_intelligence.local_liabilities_comments,
                "bank_loans_or_pending_loans": new_local_intelligence.bank_loans_or_pending_loans,
                "loan_amount": new_local_intelligence.loan_amount,
                "bank_loans_or_pending_loans_comments": new_local_intelligence.bank_loans_or_pending_loans_comments,
                "owner_mindset": new_local_intelligence.owner_mindset,
                "owner_mindset_comments": new_local_intelligence.owner_mindset_comments,
                "source_person": new_local_intelligence.source_person,
                "source_person_name": new_local_intelligence.source_person_name,
                "source_person_contact_details": new_local_intelligence.source_person_contact_details,
                "source_person_comments": new_local_intelligence.source_person_comments,
                "paper_agreement": new_local_intelligence.paper_agreement,
                "agreement_type": new_local_intelligence.agreement_type,
                "last_price_of_land": new_local_intelligence.last_price_of_land,
                "paper_agreement_comments": new_local_intelligence.paper_agreement_comments,
                "previous_transactions_on_land": new_local_intelligence.previous_transactions_on_land,
                "previous_transaction_amount": new_local_intelligence.previous_transaction_amount,
                "previous_transaction_comments": new_local_intelligence.previous_transaction_comments
            }
        }

        logger.info("Local intelligence created successfully")
        return response_data

    except Exception as e:
        logger.error(
            f"Error processing create_local_intelligence request: {e}")
        return {
            "status_code": 500,
            "message": "Failed to create local intelligence",
            "error": str(e)
        }

@app.get("/list_local_intelligences/", response_model=schemas.LocalIntelligenceListResponse)
async def list_local_intelligences(db: Session = Depends(get_db)):
    try:
        local_intelligence_records = db.query(models.LocalIntelligence).all()
        if not local_intelligence_records:
            raise HTTPException(status_code=404, detail="No local intelligence records found")

        local_intelligence_response = [
            schemas.LocalIntelligenceResponse.from_orm(record) for record in local_intelligence_records
        ]
        return {"local_intelligences": local_intelligence_response}

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error fetching records: {e}"
        )

@app.put("/update-local-intelligence/{id}", response_model=ApiResponse)
async def update_local_intelligence(id: int, request: schemas.LocalIntelligenceUpdate):
    db = SessionLocal()
    try:
        updated_local_intelligence = db.query(models.LocalIntelligence).filter(models.LocalIntelligence.id == id).first()

        if updated_local_intelligence:
            for key, value in request.dict(exclude_unset=True).items():
                setattr(updated_local_intelligence, key, value)
            db.commit()

            response_data = ApiResponse(
                status_code=200,
                message="Local intelligence updated successfully",
                data={
                    "id": updated_local_intelligence.id,
                    "issues_with_boundaries_and_owners": updated_local_intelligence.issues_with_boundaries_and_owners,
                    "issues_with_boundaries_and_owners_comments": updated_local_intelligence.issues_with_boundaries_and_owners_comments,
                    "local_liabilities": updated_local_intelligence.local_liabilities,
                    "local_liabilities_comments": updated_local_intelligence.local_liabilities_comments,
                    "bank_loans_or_pending_loans": updated_local_intelligence.bank_loans_or_pending_loans,
                    "loan_amount": updated_local_intelligence.loan_amount,
                    "bank_loans_or_pending_loans_comments": updated_local_intelligence.bank_loans_or_pending_loans_comments,
                    "owner_mindset": updated_local_intelligence.owner_mindset,
                    "owner_mindset_comments": updated_local_intelligence.owner_mindset_comments,
                    "source_person": updated_local_intelligence.source_person,
                    "source_person_name": updated_local_intelligence.source_person_name,
                    "source_person_contact_details": updated_local_intelligence.source_person_contact_details,
                    "source_person_comments": updated_local_intelligence.source_person_comments,
                    "paper_agreement": updated_local_intelligence.paper_agreement,
                    "agreement_type": updated_local_intelligence.agreement_type,
                    "last_price_of_land": updated_local_intelligence.last_price_of_land,
                    "paper_agreement_comments": updated_local_intelligence.paper_agreement_comments,
                    "previous_transactions_on_land": updated_local_intelligence.previous_transactions_on_land,
                    "previous_transaction_amount": updated_local_intelligence.previous_transaction_amount,
                    "previous_transaction_comments": updated_local_intelligence.previous_transaction_comments
                }
            )
            logger.info("Local intelligence updated successfully")
            return response_data
        else:
            raise HTTPException(
                status_code=404, detail="Local Intelligence not found")
    except Exception as e:
        logger.error(
            f"Error processing update_local_intelligence request: {e}")
        raise HTTPException(status_code=500, detail=f"An error occurred: {e}")
    finally:
        db.close()
