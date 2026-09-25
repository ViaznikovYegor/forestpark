from datetime import datetime

from sqlalchemy import DateTime, Float, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.core.db import Base, CommonMixin


class WearRecord(Base, CommonMixin):
    calculated_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, nullable=False
    )
    date_from: Mapped[datetime] = mapped_column(
        DateTime, nullable=False
    )
    date_to: Mapped[datetime] = mapped_column(
        DateTime, nullable=False
    )
    total_wear_pct: Mapped[float] = mapped_column(
        Float, nullable=False
    )
    base_wear_pct: Mapped[float] = mapped_column(
        Float, nullable=False
    )
    extra_wear_pct: Mapped[float] = mapped_column(
        Float, nullable=False
    )
    annual_rate_pct: Mapped[float] = mapped_column(
        Float, nullable=False
    )
    remaining_years: Mapped[int] = mapped_column(
        Integer, nullable=False
    )
    factor_freeze_thaw: Mapped[float] = mapped_column(
        Float, nullable=False, default=0.0
    )
    factor_precip: Mapped[float] = mapped_column(
        Float, nullable=False, default=0.0
    )
    factor_wind: Mapped[float] = mapped_column(
        Float, nullable=False, default=0.0
    )
    factor_snow: Mapped[float] = mapped_column(
        Float, nullable=False, default=0.0
    )
    factor_heat: Mapped[float] = mapped_column(
        Float, nullable=False, default=0.0
    )

    object_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey(
            'infrastructureobject.id',
            name='fk_wearrecord_infrastructureobject_id_infrastructureobject',
        ),
        nullable=True
    )
