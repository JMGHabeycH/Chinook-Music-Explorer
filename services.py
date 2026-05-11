import pandas as pd
from sqlalchemy import text
from database import get_engine

engine = get_engine()

def search_songs(keyword):
    sql = text("""
            SELECT
                t.TrackId,
                t.Name AS song,
                ar.Name AS artist,
                al.Title AS album,
                g.Name AS genre,
                t.UnitPrice AS price
            FROM Track t, Artist ar, Album al, Genre g 
            WHERE t.AlbumId = al.AlbumId
                AND al.ArtistId = ar.ArtistId
                AND t.GenreId = g.GenreId
                AND t.Name LIKE :keyword
            ORDER BY t.Name;
            """)
    return pd.read_sql(sql, engine, params={"keyword": f"%{keyword}%"})

def best_seller_songs():
    sql = text("""
                SELECT
                    t.Name AS song,
                    ar.Name AS artist,
                    al.Title AS album,
                    SUM(il.Quantity) AS total_sold,
                    ROUND(SUM(il.Quantity * il.UnitPrice), 2) AS revenue
                FROM InvoiceLine il, Track t, Album al, Artist ar
                WHERE il.TrackId = t.TrackId
                  AND t.AlbumId = al.AlbumId
                  AND al.ArtistId = ar.ArtistId
                GROUP BY t.TrackId, t.Name, ar.Name, al.Title
                ORDER BY total_sold DESC, revenue DESC
                LIMIT 10;
               """)
    
    return pd.read_sql(sql, engine)

def best_seller_albums():
    sql = text("""
                SELECT
                    al.Title AS album,
                    ar.Name AS artist,
                    SUM(il.Quantity) AS total_tracks_sold,
                    ROUND(SUM(il.Quantity * il.UnitPrice), 2) AS revenue
                FROM InvoiceLine il, Track t, Album al, Artist ar
                WHERE il.TrackId = t.TrackId
                  AND t.AlbumId = al.AlbumId
                  AND al.ArtistId = ar.ArtistId
                GROUP BY al.AlbumId, al.Title, ar.Name
                ORDER BY total_tracks_sold DESC, revenue DESC
                LIMIT 10;
               """)
    
    return pd.read_sql(sql, engine)

