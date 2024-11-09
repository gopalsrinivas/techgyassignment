from sqlalchemy import Column, Integer, Text, JSON, String
from .database import Base

class Legality(Base):
    __tablename__ = "legality"

    id = Column(Integer, primary_key=True, index=True)
    land_documents_file = Column(JSON)
    land_documents_comment = Column(Text)
    pattadhar_passbook_file = Column(JSON)
    pattadhar_passbook_comment = Column(Text)
    link_documents_file = Column(JSON)
    link_documents_comment = Column(Text)
    kasara_pahani_file = Column(JSON)
    kasara_pahani_comment = Column(Text)
    encumbrance_certificate_file = Column(JSON)
    encumbrance_comment = Column(Text)
    revenue_record_file = Column(JSON)
    revenue_record_comment = Column(Text)
    partition_deed_file = Column(JSON)
    partition_comment = Column(Text)
    faisal_patti_file = Column(JSON)
    faisal_patti_comment = Column(Text)
    death_certificate_file = Column(JSON)
    death_certificate_comment = Column(Text)
    lease_agreement_file = Column(JSON)
    lease_agreement_comment = Column(Text)
    legal_opinion_report_file = Column(JSON)
    legal_opinion_comment = Column(Text)
    land_coordinates_file = Column(JSON)
    land_coordinates_comment_file = Column(Text)
    owner_kyc_video_file = Column(JSON)
    owner_kyc_video_comment = Column(Text)


class FamilyTree(Base):
    __tablename__ = "family_tree"

    id = Column(Integer, primary_key=True, index=True)
    father_name = Column(String, index=True)
    father_age = Column(Integer)
    mother_name = Column(String, index=True)
    mother_age = Column(Integer)
    owner_name = Column(String, index=True)
    owner_age = Column(Integer)
    religion = Column(String)
    num_wifes = Column(Integer)
    num_kids = Column(Integer)
    num_siblings = Column(Integer)
