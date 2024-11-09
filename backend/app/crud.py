from sqlalchemy.orm import Session
from .models import Legality
from .schemas import LegalityCreate


def create_legality(db: Session, legality: LegalityCreate):
    db_legality = Legality(
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
