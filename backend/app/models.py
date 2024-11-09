from sqlalchemy import Column, Integer, Text, JSON, String, Boolean, Float
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


class LandBoundaries(Base):
    __tablename__ = "land_boundaries"

    id = Column(Integer, primary_key=True, index=True)
    land_images_file = Column(JSON)
    land_images_comments = Column(Text)
    landscape_view_of_farmland_file = Column(JSON)
    slope_side = Column(String)  # e.g., "North", "South", etc.
    slope_side_comments = Column(Text)
    shape_of_land = Column(String)  # e.g., "Rectangular", "Square", etc.
    shape_of_land_comment = Column(Text)   # e.g., "Water only", "Electricity only", etc.
    water_and_electricity_facility = Column(String)
    water_facility = Column(String)  # e.g., "Bore", "Municipal"
    electricity_facility = Column(String)  # e.g., "3 Phase", "2 Phase"
    water_and_electricity_facility_comments = Column(Text)
    masterplan_file = Column(JSON)
    masterplan_comments = Column(Text)
    east_boundaries_select = Column(String)  # e.g., "Road", "House", etc.
    east_owner_name = Column(String)
    east_age = Column(Integer)
    east_boundaries_comments = Column(Text)
    west_boundaries_select = Column(String)
    type_of_road = Column(String)
    width_of_road = Column(String)  # assuming width is a float value
    west_boundaries_comments = Column(Text)
    north_boundaries_select = Column(String)
    tree_count = Column(Integer)  # number of trees
    north_boundaries_comments = Column(Text)
    south_boundaries_select = Column(String)
    south_boundaries_comments = Column(Text) 
    survey_report = Column(String) # e.g., "Private Survey", "Government Survey"
    private_survey_file = Column(JSON)
    private_survey_number = Column(String)
    government_survey_file = Column(JSON)
    government_survey_number = Column(String)
    survey_report_comments = Column(Text)


class Valuation(Base):
    __tablename__ = "valuation"

    id = Column(Integer, primary_key=True, index=True)
    village_map_or_naksha_file = Column(JSON)
    village_map_or_naksha_comments = Column(Text)
    sub_register_value_file = Column(JSON)
    sub_register_value_comments = Column(Text)
    valuator_report_file = Column(JSON)
    valuator_report_comments = Column(Text)
    land_owner_value_file = Column(JSON)
    land_owner_value_comments = Column(Text)
    road_approach_type = Column(String(255))
    road_width = Column(Float)
    road_approach_comments = Column(Text)
    water_facility = Column(Boolean)
    primary_source_of_land = Column(String(255))
    water_facility_comments = Column(Text)
    recent_transaction_in_surrounding = Column(String(50))  # 'Yes', 'No', 'NA'
    valuation_per_acre = Column(Float)
    local_market_acre_price = Column(Float)
    recent_transaction_comments = Column(Text)
    electricity_facility = Column(Boolean)
    electricity_comments = Column(Text)
    existing_trees = Column(Boolean)
    tree_count = Column(Integer)
    trees_comments = Column(Text)
    surrounding_mines = Column(Boolean)
    mines_comments = Column(Text)
    disadvantages_comments = Column(Text)
    future_plans_comments = Column(Text)
    upcoming_infrastructures = Column(Boolean)
    infrastructures_list = Column(Text)  # For list of infrastructures
    infrastructures_comments = Column(Text)
    railway_connectivity = Column(Boolean)
    railway_distance = Column(Float)
    railway_comments = Column(Text)
    airport_connectivity = Column(Boolean)
    airport_distance = Column(Float)
    airport_comments = Column(Text)
