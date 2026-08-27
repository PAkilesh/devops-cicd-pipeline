CREATE TABLE IF NOT EXISTS assets (
    id SERIAL PRIMARY KEY,
    asset_id VARCHAR(50) UNIQUE NOT NULL,
    user_name VARCHAR(100),
    brand VARCHAR(100),
    model VARCHAR(100),
    status VARCHAR(50)
);

INSERT INTO assets (asset_id, user_name, brand, model, status)
VALUES
('LAP001', 'Akhil', 'Lenovo', 'ThinkPad T14', 'Assigned'),
('LAP002', 'Demo User', 'Dell', 'Latitude 3420', 'Inventory')
ON CONFLICT (asset_id) DO NOTHING;
