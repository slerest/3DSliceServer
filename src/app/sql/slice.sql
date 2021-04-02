-- name: get-all-slices
-- Get all slices
SELECT "ID",
	slice."GCODE",
	slice."PRINT_TIME",
	slice."SLICE_TIME",
	slice."STATUS",
	slice."COLOR",
	part."ID",
	part."NAME",
	part."FILE",
	part."FORMAT",
	slicer."ID",
	slicer."NAME",
	slicer."VERSION",
	material."ID",
	material."NAME",
	material."CATEGORY",
	material."SUBCATEGORY",
	material."TECHNOLOGIE_ID",
	slice."CREATED_AT",
	slice."UPDATED_AT"
FROM "3DSLICESERVER"."SLICE" as slice
		INNER JOIN "3DSLICESERVER"."PART" as part ON slice."PART_ID" = part."ID"
		INNER JOIN "3DSLICESERVER"."SLICER" as slicer ON slice."SLICER_ID" = slicer."ID"
		INNER JOIN "3DSLICESERVER"."MATERIAL" as material ON slice."MATERIAL_ID" = material."ID";

-- name: get-slice-by-id
-- Get slice by id
SELECT "ID",
	slice."GCODE",
	slice."PRINT_TIME",
	slice."SLICE_TIME",
	slice."STATUS",
	slice."COLOR",
	part."ID",
	part."NAME",
	part."FILE",
	part."FORMAT",
	slicer."ID",
	slicer."NAME",
	slicer."VERSION",
	material."ID",
	material."NAME",
	material."CATEGORY",
	material."SUBCATEGORY",
	material."TECHNOLOGIE_ID",
	slice."CREATED_AT",
	slice."UPDATED_AT"
FROM "3DSLICESERVER"."SLICE" as slice
		INNER JOIN "3DSLICESERVER"."PART" as part ON slice."PART_ID" = part."ID"
		INNER JOIN "3DSLICESERVER"."SLICER" as slicer ON slice."SLICER_ID" = slicer."ID"
		INNER JOIN "3DSLICESERVER"."MATERIAL" as material ON slice."MATERIAL_ID" = material."ID"
WHERE slice."ID" == :id;

-- name: insert-slice
-- Insert slice
INSERT INTO "3DSLICESERVER"."SLICE"(
	"GCODE",
	"PRINT_TIME",
	"SLICE_TIME",
	"STATUS",
	"COLOR",
	"PART_ID",
	"SLICER_ID",
	"MATERIAL_ID"
) VALUES (
	:gcode,
	:print_tine,
	:slice_time,
	:status,
	:color,
	:part_id,
	:slicer:id,
	:material_id
);

-- name: update-slice
-- Update slice
UPDATE "3DSLICESERVER"."SLICE"
SET
	"GCODE" = :gcode,
	"PRINT_TIME" = :print_time,
	"SLICE_TIME" = :slice_time,
	"STATUS" = :status,
	"COLOR" = :color,
	"PART_ID" = :part_id,
	"SLICER_ID" = :slicer_id,
	"MATERIAL_ID" = :material_id
WHERE
	"ID" = :id;

-- name: update-slice-after-slice
-- Update slice after slice
UPDATE "3DSLICESERVER"."SLICE"
SET
	"GCODE" = :gcode,
	"PRINT_TIME" = :print_time,
	"SLICE_TIME" = :slice_time,
	"STATUS" = :status
WHERE
	"ID" = :id;
