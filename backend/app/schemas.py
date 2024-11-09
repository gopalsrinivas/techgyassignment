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
