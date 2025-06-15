/**
ANIMAL_INS : 동물 보호소에 들어온 동물들 정보 
ANIMAL_OUTS : 동물 보호소에서 입양 보낸 동물의 정보

보호소에서 중성화 수술을 거친 동물 정보를 구하라 
보호소 올 때는 중성화 되지 않았지만 나갈 땐 중성화 된 동물의 정보 
**/

SELECT 
    AI.ANIMAL_ID,
    AI.ANIMAL_TYPE,
    AI.NAME
FROM ANIMAL_INS AI
INNER JOIN ANIMAL_OUTS AO
    ON AI.ANIMAL_ID = AO.ANIMAL_ID
WHERE 1=1
    AND AI.SEX_UPON_INTAKE LIKE '%Intact%' 
    AND (AO.SEX_UPON_OUTCOME LIKE '%Spayed%' OR AO.SEX_UPON_OUTCOME LIKE '%Neutered%')
GROUP BY
    AI.ANIMAL_ID,
    AI.ANIMAL_TYPE,
    AI.NAME
ORDER BY
        AI.ANIMAL_ID

