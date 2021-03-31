CREATE SCHEMA "3DSLICESERVER";

CREATE OR REPLACE FUNCTION trigger_set_timestamp()
RETURNS TRIGGER AS $$
BEGIN
	  NEW."UPDATED_AT" = NOW();
	  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TABLE "3DSLICESERVER"."SLICE" ( -- TODO check si on peut creer des nom de schema qui commence avec un number
	"ID" SERIAL PRIMARY KEY NOT NULL,
	"GCODE" text DEFAULT NULL,
	"PRINT_TIME" interval DEFAULT NULL,
	"SLICE_TIME" interval DEFAULT NULL,
	"PART_ID" integer DEFAULT NULL, -- foreign key
	"STATUS" varchar(50) DEFAULT NULL,
	"TECHNOLOGIE_ID" integer DEFAULT NULL,
	"COLOR" integer[] DEFAULT NULL, -- peut avoir plusieur couleur
	"SLICER_ID" integer DEFAULT NULL, -- foreign key
	"MATERIAL_ID" integer DEFAULT NULL, -- foreign key
	"CREATED_AT" timestamp without time zone NOT NULL DEFAULT now(),
	"UPDATED_AT" timestamp without time zone NOT NULL DEFAULT now()
);

CREATE TRIGGER set_timestamp_command_lines
BEFORE UPDATE ON "3DSLICESERVER"."SLICE"
FOR EACH ROW
	EXECUTE PROCEDURE trigger_set_timestamp();

CREATE TABLE "3DSLICESERVER"."TECHNOLOGIE" (
	"ID" SERIAL PRIMARY KEY NOT NULL,
	"NAME" varchar(255) NOT NULL
);

CREATE TABLE "3DSLICESERVER"."MATERIAL" (
	"ID" SERIAL PRIMARY KEY NOT NULL,
	"NAME" varchar(255) NOT NULL,
	"CATEGORY" varchar(255) DEFAULT NULL,
	"SUBCATEGORY" varchar(255) DEFAULT NULL,
	"TECHNOLOGIE" integer DEFAULT NULL -- foreign key

);

CREATE TABLE "3DSLICESERVER"."PARTS" (
	"ID" SERIAL PRIMARY KEY NOT NULL,
	"NAME" varchar(255) NOT NULL,
	"FILE" bytea,
	"FORMAT" integer --foreign key
);

CREATE TABLE "3DSLICESERVER"."FORMAT" (
	"ID" SERIAL PRIMARY KEY NOT NULL,
	"NAME" varchar(10) NOT NULL
);

