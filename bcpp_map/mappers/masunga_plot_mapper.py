from dateutil.relativedelta import MO, TU, WE, TH, FR
from datetime import date

from edc_map.site_mappers import site_mappers

from ..choices import SECTIONS, SUB_SECTIONS
from ..constants import BASELINE_SURVEY_SLUG
from ..landmarks import MASUNGA_LANDMARKS
from ..structures import ClinicDaysTuple, SurveyDatesTuple

from .base_plot_mapper import BasePlotMapper


class MasungaPlotMapper(BasePlotMapper):

    map_area = 'masunga'
    map_code = '37'
    pair = 15
    regions = SECTIONS
    sections = SUB_SECTIONS

    landmarks = MASUNGA_LANDMARKS

    intervention = True

    center_lat = -20.667218
    center_lon = 27.428340
    radius = 7.5
    location_boundary = ()

    survey_dates = {
        BASELINE_SURVEY_SLUG: SurveyDatesTuple(
            name='bhs',
            start_date=date(2015, 10, 15),
            full_enrollment_date=date(2015, 11, 30),
            end_date=date(2015, 11, 30),
            smc_start_date=date(2016, 1, 7)),
        'bcpp-year-2': SurveyDatesTuple(
            name='t1',
            start_date=date(2016, 1, 1),
            full_enrollment_date=date(2016, 2, 17),
            end_date=date(2016, 2, 22),
            smc_start_date=date(2016, 12, 22)),
        'bcpp-year-3': SurveyDatesTuple(
            name='t2',
            start_date=None,
            full_enrollment_date=None,
            end_date=None,
            smc_start_date=None),
    }

    clinic_days = {
        BASELINE_SURVEY_SLUG: {
            'IDCC': ClinicDaysTuple((MO, TU, WE, TH), None),
            'ANC': ClinicDaysTuple((MO, TU, WE, TH, FR), None),
            'VCT': ClinicDaysTuple((MO, TU, WE, TH, FR), None),
            'SMC': ClinicDaysTuple((MO, TU, WE, TH, FR), survey_dates[BASELINE_SURVEY_SLUG].smc_start_date)},
        'bcpp-year-2': {
            'IDCC': ClinicDaysTuple((MO, ), None),
            'ANC': ClinicDaysTuple((MO, TU, WE, TH, FR), None),
            'VCT': ClinicDaysTuple((MO, TU, WE, TH, FR), None),
            'SMC': ClinicDaysTuple((MO, TU, WE, TH, FR), survey_dates['bcpp-year-2'].smc_start_date)},
    }

site_mappers.register(MasungaPlotMapper)
