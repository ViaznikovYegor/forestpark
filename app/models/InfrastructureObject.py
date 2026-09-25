from datetime import datetime

from sqlalchemy import (
    String,
    Integer,
    ForeignKey,
    Table,
    Column,
    Float,
    DateTime,
    Boolean
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.db import Base, CommonMixin


material_infrastructureobject = Table(
    'material_infrastructureobject',
    Base.metadata,
    Column(
        'material_id',
        ForeignKey('material.id'),
        primary_key=True
    ),
    Column(
        'infrastructureobject_id',
        ForeignKey('infrastructureobject.id'),
        primary_key=True
    )
)


hardware_infrastructureobject = Table(
    'hardware_infrastructureobject',
    Base.metadata,
    Column(
        'hardware_id',
        ForeignKey('hardware.id'),
        primary_key=True
    ),
    Column(
        'infrastructureobject_id',
        ForeignKey('infrastructureobject.id'),
        primary_key=True
    )
)


class ObjectType(Base, CommonMixin):
    name: Mapped[str] = mapped_column(String(50), nullable=False)


class Material(Base, CommonMixin):
    name: Mapped[str] = mapped_column(String(50), nullable=False)

    infrastructure_objects: Mapped[
        list['InfrastructureObject']
    ] = relationship(
        secondary=material_infrastructureobject,
        back_populates='materials',
    )


class Hardware(Base, CommonMixin):
    name: Mapped[str] = mapped_column(String(50), nullable=False)

    infrastructure_objects: Mapped[
        list['InfrastructureObject']
    ] = relationship(
        secondary=hardware_infrastructureobject,
        back_populates='hardwares',
    )


class Section(Base, CommonMixin):
    name: Mapped[str] = mapped_column(String(80), nullable=False)
    latitude: Mapped[float] = mapped_column(Float, nullable=False)
    longitude: Mapped[float] = mapped_column(Float, nullable=False)


class InfrastructureObject(Base, CommonMixin):
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    installed_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    base_life_years: Mapped[int] = mapped_column(
        Integer, default=12, nullable=False
    )
    is_active: Mapped[bool] = mapped_column(
        Boolean, default=True, nullable=False
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, nullable=False
    )

    materials: Mapped[list['Material']] = relationship(
        secondary=material_infrastructureobject,
        back_populates='infrastructure_objects'
    )
    hardwares: Mapped[list['Hardware']] = relationship(
        secondary=hardware_infrastructureobject,
        back_populates='infrastructure_objects'
    )
    object_type: Mapped[int] = mapped_column(
        Integer,
        ForeignKey(
            'objecttype.id',
            name='fk_infrastructureobject_objecttype_id_objecttype'
        ),
        nullable=False
    )
    section: Mapped[int] = mapped_column(
        Integer,
        ForeignKey(
            'section.id',
            name='fk_infrastructureobject_section_id_section'
        ),
        nullable=False
    )
