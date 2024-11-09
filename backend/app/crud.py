# app/crud.py
from sqlalchemy.orm import Session
from . import models, schemas  # Import models and schemas
from .schemas import LegalityCreate, FamilyTreeCreate
from fastapi import HTTPException
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Function to create a Legality record
def create_legality(db: Session, legality: schemas.LegalityCreate):
    db_legality = models.Legality(
        land_documents_file=legality.land_documents_file,
        land_documents_comment=legality.land_documents_comment,
        pattadhar_passbook_file=legality.pattadhar_passbook_file,
        pattadhar_passbook_comment=legality.pattadhar_passbook_comment,
        link_documents_file=legality.link_documents_file,
        link_documents_comment=legality.link_documents_comment,
        kasara_pahani_file=legality.kasara_pahani_file,
        kasara_pahani_comment=legality.kasara_pahani_comment,
        encumbrance_certificate_file=legality.encumbrance_certificate_file,
        encumbrance_comment=legality.encumbrance_comment,
        revenue_record_file=legality.revenue_record_file,
        revenue_record_comment=legality.revenue_record_comment,
        partition_deed_file=legality.partition_deed_file,
        partition_comment=legality.partition_comment,
        faisal_patti_file=legality.faisal_patti_file,
        faisal_patti_comment=legality.faisal_patti_comment,
        death_certificate_file=legality.death_certificate_file,
        death_certificate_comment=legality.death_certificate_comment,
        lease_agreement_file=legality.lease_agreement_file,
        lease_agreement_comment=legality.lease_agreement_comment,
        legal_opinion_report_file=legality.legal_opinion_report_file,
        legal_opinion_comment=legality.legal_opinion_comment,
        land_coordinates_file=legality.land_coordinates_file,
        land_coordinates_comment_file=legality.land_coordinates_comment_file,
        owner_kyc_video_file=legality.owner_kyc_video_file,
        owner_kyc_video_comment=legality.owner_kyc_video_comment,
    )
    db.add(db_legality)
    db.commit()
    db.refresh(db_legality)
    return db_legality

# Function to create a FamilyTree record
def create_family_tree(db: Session, family_tree: schemas.FamilyTreeCreate):
    try:
        db_family_tree = models.FamilyTree(**family_tree.dict())
        db.add(db_family_tree)
        db.commit()
        db.refresh(db_family_tree)
        logger.info(f"FamilyTree created successfully with ID: {db_family_tree.id}")
        return db_family_tree
    except Exception as e:
        logger.error(f"Error creating FamilyTree record: {e}")
        raise HTTPException(status_code=500, detail="An error occurred while creating the FamilyTree record")

# Function to get all FamilyTree records
def get_family_tree(db: Session, skip: int = 0, limit: int = 100):
    try:
        family_tree_records = db.query(models.FamilyTree).offset(skip).limit(limit).all()
        logger.info(f"Retrieved {len(family_tree_records)} FamilyTree records")
        return family_tree_records
    except Exception as e:
        logger.error(f"Error retrieving FamilyTree records: {e}")
        raise HTTPException(status_code=500, detail="An error occurred while fetching FamilyTree records")


def create_land_boundaries(db: Session, land_boundaries: schemas.LandBoundariesCreate):
    db_land_boundaries = models.LandBoundaries(
        land_images_file=land_boundaries.land_images_file,
        land_images_comments=land_boundaries.land_images_comments,
        landscape_view_of_farmland_file=land_boundaries.landscape_view_of_farmland_file,
        slope_side=land_boundaries.slope_side,
        slope_side_comments=land_boundaries.slope_side_comments,
        shape_of_land=land_boundaries.shape_of_land,
        shape_of_land_comment=land_boundaries.shape_of_land_comment,
        water_and_electricity_facility=land_boundaries.water_and_electricity_facility,
        water_facility=land_boundaries.water_facility,
        electricity_facility=land_boundaries.electricity_facility,
        water_and_electricity_facility_comments=land_boundaries.water_and_electricity_facility_comments,
        masterplan_file=land_boundaries.masterplan_file,
        masterplan_comments=land_boundaries.masterplan_comments,
        east_boundaries_select=land_boundaries.east_boundaries_select,
        east_owner_name=land_boundaries.east_owner_name,
        east_age=land_boundaries.east_age,
        east_boundaries_comments=land_boundaries.east_boundaries_comments,
        west_boundaries_select=land_boundaries.west_boundaries_select,
        type_of_road=land_boundaries.type_of_road,
        width_of_road=land_boundaries.width_of_road,
        west_boundaries_comments=land_boundaries.west_boundaries_comments,
        north_boundaries_select=land_boundaries.north_boundaries_select,
        tree_count=land_boundaries.tree_count,
        north_boundaries_comments=land_boundaries.north_boundaries_comments,
        south_boundaries_select=land_boundaries.south_boundaries_select,
        south_boundaries_comments=land_boundaries.south_boundaries_comments,
        survey_report=land_boundaries.survey_report,
        private_survey_file=land_boundaries.private_survey_file,
        private_survey_number=land_boundaries.private_survey_number,
        government_survey_file=land_boundaries.government_survey_file,
        government_survey_number=land_boundaries.government_survey_number,
        survey_report_comments=land_boundaries.survey_report_comments,
    )
    db.add(db_land_boundaries)
    db.commit()
    db.refresh(db_land_boundaries)
    return db_land_boundaries
