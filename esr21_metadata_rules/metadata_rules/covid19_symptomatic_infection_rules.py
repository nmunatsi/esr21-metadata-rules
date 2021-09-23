from edc_metadata import NOT_REQUIRED, REQUIRED

from edc_constants.constants import YES
from edc_metadata_rules import CrfRule, CrfRuleGroup, register, P

app_label = 'esr21_subject'


@register()
class covid19SymptomaticInfectionsRuleGroup(CrfRuleGroup):

    sars_pcr = CrfRule(
        predicate=P('visits', 'eq', YES),
        consequence=REQUIRED,
        alternative=NOT_REQUIRED,
        target_models=[f'{app_label}.hospitalisation', ])

    class Meta:
        app_label = app_label
        source_model = f'{app_label}.covid19symptomaticinfections'
