DO $$
DECLARE
    table_record RECORD;
BEGIN
    FOR table_record IN (SELECT tablename FROM pg_tables WHERE schemaname = current_schema()) LOOP
        EXECUTE 'DROP TABLE IF EXISTS ' || table_record.tablename || ' CASCADE';
    END LOOP;
END $$;
