-- 코드를 입력하세요
SELECT ANIMAL_TYPE, COUNT(ANIMAL_TYPE)
  FROM ANIMAL_INS
GROUP BY ANIMAL_TYPE
ORDER BY DECODE(ANIMAL_TYPE, 'Cat', 1);