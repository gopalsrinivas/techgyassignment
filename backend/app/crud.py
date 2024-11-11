from sqlalchemy.orm import Session
from . import models, schemas
from .schemas import LegalityCreate, FamilyTreeCreate
from fastapi import HTTPException
import logging
from .models import *
from .schemas import *


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


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


def update_legality(db: Session, legality_id: int, legality_data: schemas.LegalityUpdate):
    db_legality = db.query(models.Legality).filter(
        models.Legality.id == legality_id).first()
    if not db_legality:
        return None

    for field, value in legality_data.dict(exclude_unset=True).items():
        setattr(db_legality, field, value)

    db.commit()
    db.refresh(db_legality)
    return db_legality


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

def get_family_tree(db: Session, skip: int = 0, limit: int = 100):
    try:
        family_tree_records = db.query(models.FamilyTree).offset(skip).limit(limit).all()
        logger.info(f"Retrieved {len(family_tree_records)} FamilyTree records")
        return family_tree_records
    except Exception as e:
        logger.error(f"Error retrieving FamilyTree records: {e}")
        raise HTTPException(status_code=500, detail="An error occurred while fetching FamilyTree records")


def update_family_tree(db: Session, family_tree_id: int, family_tree: schemas.FamilyTreeCreate):
    try:
        db_family_tree = db.query(models.FamilyTree).filter(
            models.FamilyTree.id == family_tree_id).first()
        if db_family_tree is None:
            raise HTTPException(
                status_code=404, detail="FamilyTree record not found")

        db_family_tree.father_name = family_tree.father_name
        db_family_tree.father_age = family_tree.father_age
        db_family_tree.mother_name = family_tree.mother_name
        db_family_tree.mother_age = family_tree.mother_age
        db_family_tree.owner_name = family_tree.owner_name
        db_family_tree.owner_age = family_tree.owner_age
        db_family_tree.religion = family_tree.religion
        db_family_tree.num_wifes = family_tree.num_wifes
        db_family_tree.num_kids = family_tree.num_kids
        db_family_tree.num_siblings = family_tree.num_siblings

        db.commit()
        db.refresh(db_family_tree)

        logger.info(f"FamilyTree updated successfully with ID: {db_family_tree.id}")
        return db_family_tree
    except Exception as e:
        logger.error(f"Error updating FamilyTree record: {e}")
        raise HTTPException(status_code=500, detail="An error occurred while updating the FamilyTree record")


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


def update_land_boundaries(db: Session, land_id: int, data: LandBoundariesUpdate):
    land = db.query(LandBoundaries).filter(LandBoundaries.id == land_id).first()
    if not land:
        return None
    for field, value in data.dict(exclude_unset=True).items():
        setattr(land, field, value)
    db.commit()
    db.refresh(land)
    return land


def create_valuation(db: Session, valuation: schemas.ValuationCreate):
    db_valuation = models.Valuation(
        village_map_or_naksha_file=valuation.village_map_or_naksha_file,
        village_map_or_naksha_comments=valuation.village_map_or_naksha_comments,
        sub_register_value_file=valuation.sub_register_value_file,
        sub_register_value_comments=valuation.sub_register_value_comments,
        valuator_report_file=valuation.valuator_report_file,
        valuator_report_comments=valuation.valuator_report_comments,
        land_owner_value_file=valuation.land_owner_value_file,
        land_owner_value_comments=valuation.land_owner_value_comments,
        road_approach_type=valuation.road_approach_type,
        road_width=valuation.road_width,
        road_approach_comments=valuation.road_approach_comments,
        water_facility=valuation.water_facility,
        primary_source_of_land=valuation.primary_source_of_land,
        water_facility_comments=valuation.water_facility_comments,
        recent_transaction_in_surrounding=valuation.recent_transaction_in_surrounding,
        valuation_per_acre=valuation.valuation_per_acre,
        local_market_acre_price=valuation.local_market_acre_price,
        recent_transaction_comments=valuation.recent_transaction_comments,
        electricity_facility=valuation.electricity_facility,
        electricity_comments=valuation.electricity_comments,
        existing_trees=valuation.existing_trees,
        tree_count=valuation.tree_count,
        trees_comments=valuation.trees_comments,
        surrounding_mines=valuation.surrounding_mines,
        mines_comments=valuation.mines_comments,
        disadvantages_comments=valuation.disadvantages_comments,
        future_plans_comments=valuation.future_plans_comments,
        upcoming_infrastructures=valuation.upcoming_infrastructures,
        infrastructures_list=valuation.infrastructures_list,
        infrastructures_comments=valuation.infrastructures_comments,
        railway_connectivity=valuation.railway_connectivity,
        railway_distance=valuation.railway_distance,
        railway_comments=valuation.railway_comments,
        airport_connectivity=valuation.airport_connectivity,
        airport_distance=valuation.airport_distance,
        airport_comments=valuation.airport_comments
    )
    db.add(db_valuation)
    db.commit()
    db.refresh(db_valuation)
    return db_valuation


def update_valuation(db: Session, valuation_id: int, valuation_data: schemas.ValuationCreate):
    valuation_record = db.query(models.Valuation).filter(models.Valuation.id == valuation_id).first()
    if not valuation_record:
        return None
    for key, value in valuation_data.dict(exclude_unset=True).items():
        setattr(valuation_record, key, value)
    db.commit()
    db.refresh(valuation_record)
    return valuation_record


def create_agriculture_certification(db: Session, certification_data: schemas.AgricultureCertificationCreate):
    db_certification = models.AgricultureCertification(
        local_agriculture_officer_report_file=certification_data.local_agriculture_officer_report_file,
        local_agriculture_officer_report_comments=certification_data.local_agriculture_officer_report_comments,
        last_5_years_crop_yielding_report_file=certification_data.last_5_years_crop_yielding_report_file,
        last_5_years_crop_yielding_report_comments=certification_data.last_5_years_crop_yielding_report_comments,
        soil=certification_data.soil,
        soil_comments=certification_data.soil_comments,
        types_of_crop=certification_data.types_of_crop,
        types_of_crop_comments=certification_data.types_of_crop_comments,
        types_of_crop_can_be_grown=certification_data.types_of_crop_can_be_grown,
        types_of_crop_can_be_grown_comments=certification_data.types_of_crop_can_be_grown_comments,
        ground_water_level=certification_data.ground_water_level,
        ground_water_level_comments=certification_data.ground_water_level_comments,
        current_yielding_cost=certification_data.current_yielding_cost,
        current_returns_from_yield=certification_data.current_returns_from_yield,
        current_yielding_cost_comments=certification_data.current_yielding_cost_comments,
        current_cultivation=certification_data.current_cultivation,
        current_cultivation_name=certification_data.current_cultivation_name,
        current_cultivation_contact_details=certification_data.current_cultivation_contact_details,
        current_cultivation_comments=certification_data.current_cultivation_comments,
        natural_advantages_disadvantages_comments=certification_data.natural_advantages_disadvantages_comments,
        future_crop_plans_comments=certification_data.future_crop_plans_comments,
        suggested_crop_by_green_land=certification_data.suggested_crop_by_green_land,
        best_returns=certification_data.best_returns,
        suggested_crop_comments=certification_data.suggested_crop_comments
    )
    db.add(db_certification)
    db.commit()
    db.refresh(db_certification)
    return db_certification


def update_agriculture_certification(db: Session, agriculture_certification_id: int, agriculture_certification_data: schemas.AgricultureCertificationCreate):
    agriculture_certification_record = db.query(models.AgricultureCertification).filter(models.AgricultureCertification.id == agriculture_certification_id).first()
    if not agriculture_certification_record:
        return None
    for key, value in agriculture_certification_data.dict(exclude_unset=True).items():
        setattr(agriculture_certification_record, key, value)
    db.commit()
    db.refresh(agriculture_certification_record)
    return agriculture_certification_record


def create_local_intelligence(db: Session, intelligence_data: schemas.LocalIntelligenceCreate):
    try:
        db_intelligence = models.LocalIntelligence(
            issues_with_boundaries_and_owners=intelligence_data.issues_with_boundaries_and_owners,
            issues_with_boundaries_and_owners_comments=intelligence_data.issues_with_boundaries_and_owners_comments,
            local_liabilities=intelligence_data.local_liabilities,
            local_liabilities_comments=intelligence_data.local_liabilities_comments,
            bank_loans_or_pending_loans=intelligence_data.bank_loans_or_pending_loans,
            loan_amount=intelligence_data.loan_amount,
            bank_loans_or_pending_loans_comments=intelligence_data.bank_loans_or_pending_loans_comments,
            owner_mindset=intelligence_data.owner_mindset,
            owner_mindset_comments=intelligence_data.owner_mindset_comments,
            source_person=intelligence_data.source_person,
            source_person_name=intelligence_data.source_person_name,
            source_person_contact_details=intelligence_data.source_person_contact_details,
            source_person_comments=intelligence_data.source_person_comments,
            paper_agreement=intelligence_data.paper_agreement,
            agreement_type=intelligence_data.agreement_type,
            last_price_of_land=intelligence_data.last_price_of_land,
            paper_agreement_comments=intelligence_data.paper_agreement_comments,
            previous_transactions_on_land=intelligence_data.previous_transactions_on_land,
            previous_transaction_amount=intelligence_data.previous_transaction_amount,
            previous_transaction_comments=intelligence_data.previous_transaction_comments
        )
        db.add(db_intelligence)
        db.commit()
        db.refresh(db_intelligence)
        return db_intelligence
    except Exception as e:
        db.rollback()
        raise Exception(f"Error in creating Local Intelligence: {e}")


def update_local_intelligence(db: Session, local_intelligence_id: int, local_intelligence_data: schemas.LocalIntelligenceUpdate):
    local_intelligence_record = db.query(models.LocalIntelligence).filter(
        models.LocalIntelligence.id == local_intelligence_id).first()

    if not local_intelligence_record:
        return None

    for key, value in local_intelligence_data.dict(exclude_unset=True).items():
        setattr(local_intelligence_record, key, value)

    db.commit()
    db.refresh(local_intelligence_record)
    return local_intelligence_record
