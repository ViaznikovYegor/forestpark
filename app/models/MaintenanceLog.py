from datetime import datetime

from sqlalchemy import String, Integer, ForeignKey, DateTime, Text, Float
from sqlalchemy.orm import Mapped, mapped_column

from app.core.db import Base, CommonMixin


class MaintenanceLog(Base, CommonMixin):
    maintenance_date: Mapped[datetime] = mapped_column(
        DateTime, nullable=False
    )
    maintenance_type: Mapped[str] = mapped_column(
        String(80), nullable=False
    )
    notes: Mapped[str] = mapped_column(
        Text, nullable=True
    )
    wear_pct_before: Mapped[float] = mapped_column(
        Float, nullable=False
    )
    wear_pct_after: Mapped[float] = mapped_column(
        Float, nullable=False
    )
    performed_by: Mapped[str] = mapped_column(
        String(80), nullable=False
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, nullable=False
    )

    object_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey(
            'infrastructureobject.id',
            name='''
            fk_maintenancelog_infrastructureobject_id_infrastructureobject
            ''',
        ),
        nullable=True
    )
