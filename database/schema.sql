-- نظام إدارة المبيعات والمخازن
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- جدول المستخدمين
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    full_name VARCHAR(200) NOT NULL,
    role VARCHAR(50) DEFAULT 'cashier',
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- جدول المخازن
CREATE TABLE IF NOT EXISTS warehouses (
    id SERIAL PRIMARY KEY,
    code VARCHAR(50) UNIQUE NOT NULL,
    name VARCHAR(200) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- جدول التصنيفات
CREATE TABLE IF NOT EXISTS categories (
    id SERIAL PRIMARY KEY,
    name VARCHAR(200) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- جدول الوحدات
CREATE TABLE IF NOT EXISTS units (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    symbol VARCHAR(20) NOT NULL
);

-- جدول المنتجات
CREATE TABLE IF NOT EXISTS products (
    id SERIAL PRIMARY KEY,
    code VARCHAR(100) UNIQUE NOT NULL,
    barcode VARCHAR(100),
    name VARCHAR(300) NOT NULL,
    category_id INTEGER REFERENCES categories(id),
    unit_id INTEGER REFERENCES units(id),
    cost_price DECIMAL(15,3) DEFAULT 0,
    selling_price_1 DECIMAL(15,3) DEFAULT 0,
    selling_price_2 DECIMAL(15,3) DEFAULT 0,
    min_stock_level INTEGER DEFAULT 10,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- جدول المخزون
CREATE TABLE IF NOT EXISTS product_stock (
    id SERIAL PRIMARY KEY,
    product_id INTEGER REFERENCES products(id),
    warehouse_id INTEGER REFERENCES warehouses(id),
    quantity DECIMAL(15,3) DEFAULT 0,
    UNIQUE(product_id, warehouse_id)
);

-- جدول العملاء
CREATE TABLE IF NOT EXISTS customers (
    id SERIAL PRIMARY KEY,
    code VARCHAR(50) UNIQUE,
    name VARCHAR(300) NOT NULL,
    phone VARCHAR(20),
    current_balance DECIMAL(15,3) DEFAULT 0,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- البيانات الأولية
INSERT INTO users (username, password_hash, full_name, role) 
VALUES ('admin', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/X4xOVKj1g3X4FQ5Iu', 'مدير النظام', 'admin')
ON CONFLICT DO NOTHING;

INSERT INTO warehouses (code, name) VALUES ('WH001', 'المخزن الرئيسي') ON CONFLICT DO NOTHING;
INSERT INTO units (name, symbol) VALUES ('قطعة', 'قطعة'), ('كجم', 'كجم') ON CONFLICT DO NOTHING;
INSERT INTO categories (name) VALUES ('عام') ON CONFLICT DO NOTHING;
INSERT INTO customers (code, name) VALUES ('CASH', 'عميل نقدي') ON CONFLICT DO NOTHING;
