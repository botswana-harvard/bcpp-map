from dateutil.relativedelta import MO, TU, WE, TH, FR
from datetime import date

from edc_map.site_mappers import site_mappers

from ..choices import SECTIONS, SUB_SECTIONS
from ..constants import BASELINE_SURVEY_SLUG
from ..landmarks import TSETSEBJWE_LANDMARKS
from ..structures import ClinicDaysTuple, SurveyDatesTuple

from .base_plot_mapper import BasePlotMapper


class TsetsebjwePlotMapper(BasePlotMapper):

    map_area = 'tsetsebjwe'
    map_code = '40'
    pair = 14
    regions = SECTIONS
    sections = SUB_SECTIONS

    landmarks = TSETSEBJWE_LANDMARKS

    intervention = False

    gps_center_lat = -22.41391
    gps_center_lon = 28.39465
    radius = 5.5
    location_boundary = ()

    survey_dates = {
        BASELINE_SURVEY_SLUG: SurveyDatesTuple(
            name='bhs',
            start_date=date(2015, 9, 9),
            full_enrollment_date=date(2015, 10, 7),
            end_date=date(2015, 10, 28),
            smc_start_date=date(2015, 9, 9)),
        'bcpp-year-2': SurveyDatesTuple(
            name='t1',
            start_date=date(2015, 11, 21),
            full_enrollment_date=date(2015, 12, 17),
            end_date=date(2015, 12, 22),
            smc_start_date=date(2015, 12, 22)),
        'bcpp-year-3': SurveyDatesTuple(
            name='t2',
            start_date=None,
            full_enrollment_date=None,
            end_date=None,
            smc_start_date=None),
    }

    clinic_days = {
        BASELINE_SURVEY_SLUG: {
            'IDCC': ClinicDaysTuple((WE, ), None),
            'ANC': ClinicDaysTuple((MO, TU, WE, TH, FR), None),
            'VCT': ClinicDaysTuple((MO, TU, WE, TH, FR), None),
            'SMC': ClinicDaysTuple((MO, TU, WE, TH, FR), survey_dates[BASELINE_SURVEY_SLUG].smc_start_date)},
        'bcpp-year-2': {
            'IDCC': ClinicDaysTuple((MO, ), None),
            'ANC': ClinicDaysTuple((MO, TU, WE, TH, FR), None),
            'VCT': ClinicDaysTuple((MO, TU, WE, TH, FR), None),
            'SMC': ClinicDaysTuple((MO, TU, WE, TH, FR), survey_dates['bcpp-year-2'].smc_start_date)},
    }

site_mappers.register(TsetsebjwePlotMapper)
