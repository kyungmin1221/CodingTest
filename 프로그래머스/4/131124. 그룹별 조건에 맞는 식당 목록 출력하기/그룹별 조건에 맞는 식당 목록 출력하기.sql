SELECT 
    MEMBER_NAME,
    REVIEW_TEXT,
    DATE_FORMAT(REVIEW_DATE, '%Y-%m-%d')
FROM MEMBER_PROFILE AS MP
INNER JOIN REST_REVIEW AS RR
    ON MP.MEMBER_ID = RR.MEMBER_ID 
WHERE 1=1 
    AND RR.MEMBER_ID IN 
    ( SELECT MEMBER_ID
     FROM REST_REVIEW
     GROUP BY MEMBER_ID
     HAVING COUNT(*) = ( SELECT 
                            MAX(C) 
                         FROM ( SELECT COUNT(*) AS C 
                                FROM REST_REVIEW
                                GROUP BY MEMBER_ID
                              ) t
                       ) 
     )
     ORDER BY REVIEW_DATE ASC, REVIEW_TEXT ASC