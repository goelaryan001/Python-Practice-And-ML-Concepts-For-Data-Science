WITH active_borrows AS (
    SELECT
        book_id,
        COUNT(*) AS current_borrowers
    FROM borrowing_records
    WHERE return_date IS NULL
    GROUP BY book_id
)
SELECT
    lb.book_id,
    lb.title,
    lb.author,
    lb.genre,
    lb.publication_year,
    ab.current_borrowers
FROM library_books lb
JOIN active_borrows ab
    ON lb.book_id = ab.book_id
WHERE ab.current_borrowers = lb.total_copies
ORDER BY ab.current_borrowers DESC, lb.title ASC;