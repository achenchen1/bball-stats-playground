CREATE TABLE test_table (
    quarter_id INTEGER PRIMARY KEY,
    game_id INTEGER NOT NULL,
    player_id INTEGER NOT NULL,
    mp INTEGER,
    fg INTEGER,
    fga INTEGER,
    fg_pct REAL,
    fg3 INTEGER,
    fg3a INTEGER,
    fg3_pct REAL,
    ft INTEGER,
    fta INTEGER,
    ft_pct REAL,
    orb INTEGER,
    drb INTEGER,
    trb INTEGER,
    ast INTEGER,
    stl INTEGER,
    blk INTEGER,
    tov INTEGER,
    pf INTEGER,
    pts INTEGER,
    plus_minus REAL
);

