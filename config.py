"""
ملف إعدادات النظام
Sales & Inventory Management System Configuration
"""

import os
from dataclasses import dataclass
from typing import Optional
from dotenv import load_dotenv

load_dotenv()


@dataclass
class DatabaseConfig:
    """إعدادات قاعدة البيانات"""
    host: str = os.getenv('DB_HOST', 'localhost')
    port: int = int(os.getenv('DB_PORT', 5432))
    database: str = os.getenv('DB_NAME', 'sales_inventory_db')
    user: str = os.getenv('DB_USER', 'postgres')
    password: str = os.getenv('DB_PASSWORD', 'postgres')
    
    @property
    def connection_string(self) -> str:
        return f"postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"


@dataclass
class AppConfig:
    """إعدادات التطبيق العامة"""
    app_name: str = "نظام إدارة المبيعات والمخازن"
    app_version: str = "1.0.0"
    company_name: str = "شركتك"
    currency: str = "ر.س"
    vat_rate: float = 0.15
    low_stock_threshold: int = 10
    date_format: str = "yyyy-MM-dd"
    datetime_format: str = "yyyy-MM-dd HH:mm:ss"
    language: str = "ar"
    theme: str = "dark"


# إنشاء الإعدادات العامة
DB_CONFIG = DatabaseConfig()
APP_CONFIG = AppConfig()
