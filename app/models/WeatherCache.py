from datetime import datetime

from sqlalchemy import DateTime, Float
from sqlalchemy.orm import Mapped, mapped_column

from app.core.db import Base, CommonMixin


class WeatherCache(Base, CommonMixin):
    date: Mapped[datetime] = mapped_column(
        DateTime, nullable=False
    )
    latitude: Mapped[float] = mapped_column(
        Float, nullable=False
    )
    longitude: Mapped[float] = mapped_column(
        Float, nullable=False
    )
    temperature_max: Mapped[float] = mapped_column(
        Float, nullable=False
    )
    temperature_min: Mapped[float] = mapped_column(
        Float, nullable=False
    )
    precip_mm: Mapped[float] = mapped_column(
        Float, nullable=False
    )
    wind_ms: Mapped[float] = mapped_column(
        Float, nullable=False
    )
    snow_m: Mapped[float] = mapped_column(
        Float, nullable=False
    )
    fetched_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, nullable=False
    )
