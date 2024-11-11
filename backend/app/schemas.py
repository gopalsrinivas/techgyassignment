from pydantic import BaseModel
from typing import List, Optional

class LegalityBase(BaseModel):
    land_documents_file: Optional[List[str]] = None
    land_documents_comment: Optional[str] = None
    pattadhar_passbook_file: Optional[List[str]] = None
    pattadhar_passbook_comment: Optional[str] = None
    link_documents_file: Optional[List[str]] = None
    link_documents_comment: Optional[str] = None
    kasara_pahani_file: Optional[List[str]] = None
    kasara_pahani_comment: Optional[str] = None
    encumbrance_certificate_file: Optional[List[str]] = None
    encumbrance_comment: Optional[str] = None
    revenue_record_file: Optional[List[str]] = None
    revenue_record_comment: Optional[str] = None
    partition_deed_file: Optional[List[str]] = None
    partition_comment: Optional[str] = None
    faisal_patti_file: Optional[List[str]] = None
    faisal_patti_comment: Optional[str] = None
    death_certificate_file: Optional[List[str]] = None
    death_certificate_comment: Optional[str] = None
    lease_agreement_file: Optional[List[str]] = None
    lease_agreement_comment: Optional[str] = None
    legal_opinion_report_file: Optional[List[str]] = None
    legal_opinion_comment: Optional[str] = None
    land_coordinates_file: Optional[List[str]] = None
    land_coordinates_comment_file: Optional[str] = None
    owner_kyc_video_file: Optional[List[str]] = None
    owner_kyc_video_comment: Optional[str] = None

    class Config:
        from_attributes = True
class LegalityCreate(LegalityBase):
    pass
class LegalityUpdate(LegalityBase):
    pass

class LegalityResponse(BaseModel):
    id: int
    land_documents_file: Optional[List[str]] = None
    land_documents_comment: Optional[str] = None
    pattadhar_passbook_file: Optional[List[str]] = None
    pattadhar_passbook_comment: Optional[str] = None
    link_documents_file: Optional[List[str]] = None
    link_documents_comment: Optional[str] = None
    kasara_pahani_file: Optional[List[str]] = None
    kasara_pahani_comment: Optional[str] = None
    encumbrance_certificate_file: Optional[List[str]] = None
    encumbrance_comment: Optional[str] = None
    revenue_record_file: Optional[List[str]] = None
    revenue_record_comment: Optional[str] = None
    partition_deed_file: Optional[List[str]] = None
    partition_comment: Optional[str] = None
    faisal_patti_file: Optional[List[str]] = None
    faisal_patti_comment: Optional[str] = None
    death_certificate_file: Optional[List[str]] = None
    death_certificate_comment: Optional[str] = None
    lease_agreement_file: Optional[List[str]] = None
    lease_agreement_comment: Optional[str] = None
    legal_opinion_report_file: Optional[List[str]] = None
    legal_opinion_comment: Optional[str] = None
    land_coordinates_file: Optional[List[str]] = None
    land_coordinates_comment_file: Optional[str] = None
    owner_kyc_video_file: Optional[List[str]] = None
    owner_kyc_video_comment: Optional[str] = None
    class Config:
        from_attributes = True
class LegalityListResponse(BaseModel):
    legality: List[LegalityResponse]
    class Config:
        from_attributes = True
        
class FamilyTreeCreate(BaseModel):
    father_name: str
    father_age: int
    mother_name: str
    mother_age: int
    owner_name: str
    owner_age: int
    religion: str
    num_wifes: int
    num_kids: int
    num_siblings: int

class FamilyTreeResponse(FamilyTreeCreate):
    id: int
    class Config:
        from_attributes = True

class FamilyTreeListResponse(BaseModel):
    family_tree: List[FamilyTreeResponse]

class ApiResponse(BaseModel):
    status_code: int
    message: str
    data: dict

class LandBoundariesCreate(BaseModel):
    land_images_file: Optional[List[str]] = None
    land_images_comments: Optional[str] = None
    landscape_view_of_farmland_file: Optional[List[str]] = None
    slope_side: Optional[str] = None
    slope_side_comments: Optional[str] = None
    shape_of_land: Optional[str] = None
    shape_of_land_comment: Optional[str] = None
    water_and_electricity_facility: Optional[str] = None
    water_facility: Optional[str] = None
    electricity_facility: Optional[str] = None
    water_and_electricity_facility_comments: Optional[str] = None
    masterplan_file: Optional[List[str]] = None
    masterplan_comments: Optional[str] = None
    east_boundaries_select: Optional[str] = None
    east_owner_name: Optional[str] = None
    east_age: Optional[int] = None
    east_boundaries_comments: Optional[str] = None
    west_boundaries_select: Optional[str] = None
    type_of_road: Optional[str] = None
    width_of_road: Optional[float] = None
    west_boundaries_comments: Optional[str] = None
    north_boundaries_select: Optional[str] = None
    tree_count: Optional[int] = None
    north_boundaries_comments: Optional[str] = None
    south_boundaries_select: Optional[str] = None
    south_boundaries_comments: Optional[str] = None
    survey_report: Optional[str] = None
    private_survey_file: Optional[List[str]] = None
    private_survey_number: Optional[str] = None
    government_survey_file: Optional[List[str]] = None
    government_survey_number: Optional[str] = None
    survey_report_comments: Optional[str] = None

    class Config:
        from_attributes = True
class LandBoundariesResponse(LandBoundariesCreate):
    id: int
    class Config:
        from_attributes = True

class LandBoundariesListResponse(BaseModel):
    land_boundaries: List[LandBoundariesResponse]
    class Config:
        from_attributes = True

class LandBoundariesUpdate(LandBoundariesCreate):
    pass

class ValuationCreate(BaseModel):
    village_map_or_naksha_file: Optional[List[str]] = None
    village_map_or_naksha_comments: Optional[str] = None
    sub_register_value_file: Optional[List[str]] = None
    sub_register_value_comments: Optional[str] = None
    valuator_report_file: Optional[List[str]] = None
    valuator_report_comments: Optional[str] = None
    land_owner_value_file: Optional[List[str]] = None
    land_owner_value_comments: Optional[str] = None
    road_approach_type: Optional[str] = None
    road_width: Optional[float] = None
    road_approach_comments: Optional[str] = None
    water_facility: Optional[bool] = None
    primary_source_of_land: Optional[str] = None
    water_facility_comments: Optional[str] = None
    recent_transaction_in_surrounding: Optional[str] = None
    valuation_per_acre: Optional[float] = None
    local_market_acre_price: Optional[float] = None
    recent_transaction_comments: Optional[str] = None
    electricity_facility: Optional[bool] = None
    electricity_comments: Optional[str] = None
    existing_trees: Optional[bool] = None
    tree_count: Optional[int] = None
    trees_comments: Optional[str] = None
    surrounding_mines: Optional[bool] = None
    mines_comments: Optional[str] = None
    disadvantages_comments: Optional[str] = None
    future_plans_comments: Optional[str] = None
    upcoming_infrastructures: Optional[bool] = None
    infrastructures_list: Optional[str] = None
    infrastructures_comments: Optional[str] = None
    railway_connectivity: Optional[bool] = None
    railway_distance: Optional[float] = None
    railway_comments: Optional[str] = None
    airport_connectivity: Optional[bool] = None
    airport_distance: Optional[float] = None
    airport_comments: Optional[str] = None

    class Config:
        from_attributes = True

class ValuationResponse(BaseModel):
    id: int
    village_map_or_naksha_file: Optional[List[str]] = None
    village_map_or_naksha_comments: Optional[str] = None
    sub_register_value_file: Optional[List[str]] = None
    sub_register_value_comments: Optional[str] = None
    valuator_report_file: Optional[List[str]] = None
    valuator_report_comments: Optional[str] = None
    land_owner_value_file: Optional[List[str]] = None
    land_owner_value_comments: Optional[str] = None
    road_approach_type: Optional[str] = None
    road_width: Optional[float] = None
    road_approach_comments: Optional[str] = None
    water_facility: Optional[bool] = None
    primary_source_of_land: Optional[str] = None
    water_facility_comments: Optional[str] = None
    recent_transaction_in_surrounding: Optional[str] = None
    valuation_per_acre: Optional[float] = None
    local_market_acre_price: Optional[float] = None
    recent_transaction_comments: Optional[str] = None
    electricity_facility: Optional[bool] = None
    electricity_comments: Optional[str] = None
    existing_trees: Optional[bool] = None
    tree_count: Optional[int] = None
    trees_comments: Optional[str] = None
    surrounding_mines: Optional[bool] = None
    mines_comments: Optional[str] = None
    disadvantages_comments: Optional[str] = None
    future_plans_comments: Optional[str] = None
    upcoming_infrastructures: Optional[bool] = None
    infrastructures_list: Optional[str] = None
    infrastructures_comments: Optional[str] = None
    railway_connectivity: Optional[bool] = None
    railway_distance: Optional[float] = None
    railway_comments: Optional[str] = None
    airport_connectivity: Optional[bool] = None
    airport_distance: Optional[float] = None
    airport_comments: Optional[str] = None

    class Config:
        from_attributes = True
class ValuationListResponse(BaseModel):
    valuations: List[ValuationResponse]

    class Config:
        from_attributes = True
class ValuationUpdate(ValuationCreate):
    pass
class AgricultureCertificationCreate(BaseModel):
    local_agriculture_officer_report_file: Optional[List[str]] = None
    local_agriculture_officer_report_comments: Optional[str] = None
    last_5_years_crop_yielding_report_file: Optional[List[str]] = None
    last_5_years_crop_yielding_report_comments: Optional[str] = None
    soil: Optional[str] = None
    soil_comments: Optional[str] = None
    types_of_crop: Optional[str] = None
    types_of_crop_comments: Optional[str] = None
    types_of_crop_can_be_grown: Optional[str] = None
    types_of_crop_can_be_grown_comments: Optional[str] = None
    ground_water_level: Optional[str] = None
    ground_water_level_comments: Optional[str] = None
    current_yielding_cost: Optional[int] = None
    current_returns_from_yield: Optional[int] = None
    current_yielding_cost_comments: Optional[str] = None
    current_cultivation: Optional[str] = None
    current_cultivation_name: Optional[str] = None
    current_cultivation_contact_details: Optional[str] = None
    current_cultivation_comments: Optional[str] = None
    natural_advantages_disadvantages_comments: Optional[str] = None
    future_crop_plans_comments: Optional[str] = None
    suggested_crop_by_green_land: Optional[str] = None
    best_returns: Optional[int] = None
    suggested_crop_comments: Optional[str] = None

    class Config:
        from_attributes = True

class AgricultureCertificationResponse(BaseModel):
    id: int
    local_agriculture_officer_report_file: Optional[List[str]] = None
    local_agriculture_officer_report_comments: Optional[str] = None
    last_5_years_crop_yielding_report_file: Optional[List[str]] = None
    last_5_years_crop_yielding_report_comments: Optional[str] = None
    soil: Optional[str] = None
    soil_comments: Optional[str] = None
    types_of_crop: Optional[str] = None
    types_of_crop_comments: Optional[str] = None
    types_of_crop_can_be_grown: Optional[str] = None
    types_of_crop_can_be_grown_comments: Optional[str] = None
    ground_water_level: Optional[str] = None
    ground_water_level_comments: Optional[str] = None
    current_yielding_cost: Optional[int] = None
    current_returns_from_yield: Optional[int] = None
    current_yielding_cost_comments: Optional[str] = None
    current_cultivation: Optional[str] = None
    current_cultivation_name: Optional[str] = None
    current_cultivation_contact_details: Optional[str] = None
    current_cultivation_comments: Optional[str] = None
    natural_advantages_disadvantages_comments: Optional[str] = None
    future_crop_plans_comments: Optional[str] = None
    suggested_crop_by_green_land: Optional[str] = None
    best_returns: Optional[int] = None
    suggested_crop_comments: Optional[str] = None

    class Config:
        from_attributes = True

class AgricultureCertificationListResponse(BaseModel):
    agriculture_certifications: List[AgricultureCertificationResponse]

class AgricultureCertificationUpdate(AgricultureCertificationCreate):
    pass

class LocalIntelligenceBase(BaseModel):
    issues_with_boundaries_and_owners: Optional[str] = None
    issues_with_boundaries_and_owners_comments: Optional[str] = None
    local_liabilities: Optional[str] = None
    local_liabilities_comments: Optional[str] = None
    bank_loans_or_pending_loans: Optional[str] = None
    loan_amount: Optional[int] = None
    bank_loans_or_pending_loans_comments: Optional[str] = None
    owner_mindset: Optional[str] = None
    owner_mindset_comments: Optional[str] = None
    source_person: Optional[str] = None
    source_person_name: Optional[str] = None
    source_person_contact_details: Optional[str] = None
    source_person_comments: Optional[str] = None
    paper_agreement: Optional[str] = None
    agreement_type: Optional[str] = None
    last_price_of_land: Optional[int] = None
    paper_agreement_comments: Optional[str] = None
    previous_transactions_on_land: Optional[str] = None
    previous_transaction_amount: Optional[int] = None
    previous_transaction_comments: Optional[str] = None

class LocalIntelligenceCreate(LocalIntelligenceBase):
    pass

class LocalIntelligenceResponse(LocalIntelligenceBase):
    id: int
    class Config:
       from_attributes = True

class LocalIntelligenceUpdate(LocalIntelligenceBase):
    pass


class LocalIntelligenceListResponse(BaseModel):
    local_intelligences: List[LocalIntelligenceResponse]

    class Config:
        from_attributes = True
