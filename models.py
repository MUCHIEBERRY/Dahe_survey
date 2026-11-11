from sqlmodel import Field , SQLModel

class Player(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    main_character: str
    weapon: str
    highest_damage: float
    favorite_element: str
    favorite_nation: str
    favorite_archon: str
    year_started: int
    adventure_level: int
    favorite_harbinger: str
    favorite_adeptus: str






