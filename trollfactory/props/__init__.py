"""Properties generation scripts used by the TrollFactory cli and library."""

__props__: list[str] = [
    'address',
    'bank',
    'birthdate',
    'blood_type',
    'car',
    'cc',
    'colors',
    'document_id',
    'gender',
    'language',
    'measurements',
    'name',
    'online',
    'ssn',
    'phone',
]

__all__: list[str] = __props__ + ['langs']
