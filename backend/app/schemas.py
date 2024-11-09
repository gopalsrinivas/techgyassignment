from pydantic import BaseModel
from typing import List, Optional

class LegalityCreate(BaseModel):
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
    survey_report_comments: Optional[str] = None

    class Config:
        from_attributes = True

class LandBoundariesResponse(BaseModel):
    id: int
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
    survey_report_comments: Optional[str] = None

    class Config:
        from_attributes = True

class LandBoundariesListResponse(BaseModel):
    land_boundaries: List[LandBoundariesResponse]

    class Config:
        from_attributes = True
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


class LandBoundariesResponse(BaseModel):
    id: int
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


class LandBoundariesListResponse(BaseModel):
    land_boundaries: List[LandBoundariesResponse]

    class Config:
        from_attributes = True
