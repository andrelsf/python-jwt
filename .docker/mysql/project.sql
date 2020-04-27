CREATE SCHEMA `ProjectX`;

CREATE TABLE `ProjectX`.company ( 
	company_id           int  NOT NULL    PRIMARY KEY,
	company_name         varchar(100)  NOT NULL    
 );

CREATE TABLE `ProjectX`.financial_control ( 
	financial_id         int  NOT NULL    PRIMARY KEY,
	company_id           int  NOT NULL    ,
	user_id              int  NOT NULL    ,
	partner_id           int  NOT NULL    ,
	data_emissao         date      ,
	financial_value      float(12,0)      
 ) engine=InnoDB;

ALTER TABLE `ProjectX`.financial_control COMMENT 'Controle Financeiro';

CREATE TABLE `ProjectX`.map_action ( 
	action_id            int  NOT NULL    PRIMARY KEY,
	action_description   varchar(100)  NOT NULL    ,
	action_data          blob  NOT NULL    
 ) engine=InnoDB;

CREATE TABLE `ProjectX`.map_flow ( 
	flow_id              int  NOT NULL    PRIMARY KEY,
	flow_name            varchar(100)  NOT NULL    ,
	flow_description     varchar(100)  NOT NULL    ,
	flow_data            json  NOT NULL    
 ) engine=InnoDB;

ALTER TABLE `ProjectX`.map_flow COMMENT 'Mapa de Fluxo';

CREATE TABLE `ProjectX`.map_form_table ( 
	form_id              int  NOT NULL    PRIMARY KEY,
	form_name            varchar(100)  NOT NULL    ,
	table_name           varchar(100)  NOT NULL    ,
	form_description     varchar(100)  NOT NULL    ,
	primary_keys         varchar(100)  NOT NULL    ,
	only_form            varchar(1)      ,
	form_main_id         int      ,
	fgcolor_grid         varchar(500)      ,
	bkcolor_grid         varchar(500)      ,
	additional           varchar(1)      
 ) engine=InnoDB;

ALTER TABLE `ProjectX`.map_form_table COMMENT 'Mapa de Formulários/Tabelas.';

ALTER TABLE `ProjectX`.map_form_table MODIFY primary_keys varchar(100)  NOT NULL   COMMENT 'chaves separadas por virgula';

ALTER TABLE `ProjectX`.map_form_table MODIFY only_form varchar(1)     COMMENT 'S/N';

ALTER TABLE `ProjectX`.map_form_table MODIFY fgcolor_grid varchar(500)     COMMENT 'Se vazio cor padrão ou expressão para paleta de cores EXADecimal.';

ALTER TABLE `ProjectX`.map_form_table MODIFY bkcolor_grid varchar(500)     COMMENT 'Se vazio cor padrão ou expressão para paleta de cores EXADecimal.';

ALTER TABLE `ProjectX`.map_form_table MODIFY additional varchar(1)     COMMENT 'S/N';

CREATE TABLE `ProjectX`.map_relationship_form ( 
	form_id_orig         int  NOT NULL    ,
	form_id_dest         int  NOT NULL    ,
	relationship_name    varchar(100)  NOT NULL    ,
	CONSTRAINT pk_map_relationship_form PRIMARY KEY ( form_id_orig, form_id_dest ),
	CONSTRAINT fk_map_relationship_form_orig FOREIGN KEY ( form_id_orig ) REFERENCES `ProjectX`.map_form_table( form_id ) ON DELETE NO ACTION ON UPDATE NO ACTION,
	CONSTRAINT fk_map_relationship_form_dest FOREIGN KEY ( form_id_dest ) REFERENCES `ProjectX`.map_form_table( form_id ) ON DELETE NO ACTION ON UPDATE NO ACTION
 ) engine=InnoDB;

CREATE INDEX fk_map_relationship_form_dest ON `ProjectX`.map_relationship_form ( form_id_dest );

CREATE TABLE `ProjectX`.`order` ( 
	order_id             int  NOT NULL    PRIMARY KEY,
	company_id           int  NOT NULL    ,
	user_id              int  NOT NULL    ,
	partner_id           int  NOT NULL    ,
	data_emissao         date      ,
	financial_value      float(12,0)      
 );

ALTER TABLE `ProjectX`.`order` COMMENT 'Controle Financeiro';

CREATE TABLE `ProjectX`.partner ( 
	partner_id           int  NOT NULL    PRIMARY KEY,
	partner_name         varchar(100)  NOT NULL    
 ) engine=InnoDB;

CREATE TABLE `ProjectX`.`user` ( 
	user_id              int  NOT NULL    PRIMARY KEY,
	user_name            varchar(100)  NOT NULL    
 );

CREATE TABLE `ProjectX`.map_field ( 
	field_id             int  NOT NULL    PRIMARY KEY,
	form_id              int  NOT NULL    ,
	field_name           varchar(50)  NOT NULL    ,
	field_description    varchar(100)  NOT NULL    ,
	field_presentation   varchar(50)  NOT NULL    ,
	field_order          int  NOT NULL    ,
	CONSTRAINT fk_map_field_map_form_table FOREIGN KEY ( form_id ) REFERENCES `ProjectX`.map_form_table( form_id ) ON DELETE NO ACTION ON UPDATE NO ACTION
 ) engine=InnoDB;

CREATE INDEX fk_map_field_map_form_table ON `ProjectX`.map_field ( form_id );

ALTER TABLE `ProjectX`.map_field COMMENT 'Mapa de Campos';

CREATE TABLE `ProjectX`.map_option_field ( 
	field_id             int  NOT NULL    PRIMARY KEY,
	field_value_bd       varchar(50)  NOT NULL    ,
	field_value_app      varchar(100)  NOT NULL    ,
	field_value_order    int  NOT NULL    ,
	CONSTRAINT fk_map_option_field_map_field FOREIGN KEY ( field_id ) REFERENCES `ProjectX`.map_field( field_id ) ON DELETE NO ACTION ON UPDATE NO ACTION
 ) engine=InnoDB;

CREATE TABLE `ProjectX`.map_propriety_field ( 
	field_id             int  NOT NULL    ,
	field_propriety      varchar(100)  NOT NULL    ,
	field_value          varchar(500)      ,
	CONSTRAINT pk_map_propriety_field PRIMARY KEY ( field_id, field_propriety ),
	CONSTRAINT fk_map_propriety_field_map_field FOREIGN KEY ( field_id ) REFERENCES `ProjectX`.map_field( field_id ) ON DELETE NO ACTION ON UPDATE NO ACTION
 ) engine=InnoDB;
