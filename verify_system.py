#!/usr/bin/env python
"""
System Verification Script - Checks all components are working
"""
import sys
from pathlib import Path

# Add to path
sys.path.insert(0, str(Path(__file__).parent))

def check_files():
    """Verify all required files exist"""
    print("\n📁 Checking files...")
    base_dir = Path(__file__).parent
    
    required_files = [
        "app.py",
        "config.py",
        "models.py",
        "utils.py",
        "requirements.txt",
        "model/project3/cc_fraud_rf.pkl",
        "model/project3/loan_default_rf.pkl",
        "model/project3/iso_forest.pkl",
        "model/project3/spend_kmeans.pkl",
        "creditcard.csv",
        "loan_data.csv",
        "bank_transactions_data_2.csv",
    ]
    
    all_exist = True
    for file in required_files:
        path = base_dir / file
        if path.exists():
            print(f"  ✅ {file}")
        else:
            print(f"  ❌ {file}")
            all_exist = False
    
    return all_exist

def check_imports():
    """Verify all Python imports work"""
    print("\n📦 Checking imports...")
    imports = [
        ("flask", "Flask"),
        ("sqlalchemy", "SQLAlchemy"),
        ("joblib", "joblib"),
        ("pandas", "pandas"),
        ("numpy", "numpy"),
        ("sklearn", "scikit-learn"),
    ]
    
    all_ok = True
    for module, name in imports:
        try:
            __import__(module)
            print(f"  ✅ {name}")
        except ImportError as e:
            print(f"  ❌ {name}: {e}")
            all_ok = False
    
    return all_ok

def check_models():
    """Verify ML models can be loaded"""
    print("\n🤖 Checking models...")
    import joblib
    from pathlib import Path
    
    base_dir = Path(__file__).parent
    model_dir = base_dir / "model" / "project3"
    
    models_to_check = [
        ("cc_fraud_rf.pkl", "Credit Card Fraud RF"),
        ("loan_default_rf.pkl", "Loan Default"),
        ("iso_forest.pkl", "Isolation Forest"),
        ("spend_kmeans.pkl", "KMeans Spending"),
    ]
    
    all_ok = True
    for model_file, name in models_to_check:
        try:
            path = model_dir / model_file
            model = joblib.load(path)
            print(f"  ✅ {name}")
        except Exception as e:
            print(f"  ❌ {name}: {e}")
            all_ok = False
    
    return all_ok

def check_config():
    """Verify configuration"""
    print("\n⚙️  Checking configuration...")
    try:
        from config import (
            DATABASE_URI, SECRET_KEY, MODEL_DIR, 
            DEMO_USERS, FRAUD_THRESHOLDS
        )
        print(f"  ✅ Database: {DATABASE_URI}")
        print(f"  ✅ Model Dir: {MODEL_DIR}")
        print(f"  ✅ Demo Users: {len(DEMO_USERS)} users")
        print(f"  ✅ Fraud Thresholds configured")
        return True
    except Exception as e:
        print(f"  ❌ Config error: {e}")
        return False

def check_database():
    """Verify database connection"""
    print("\n🗄️  Checking database...")
    try:
        from app import app, db
        with app.app_context():
            db.create_all()
            print(f"  ✅ Database initialized")
            return True
    except Exception as e:
        print(f"  ❌ Database error: {e}")
        return False

def check_ml_manager():
    """Verify ML Manager works"""
    print("\n⚡ Checking ML Manager...")
    try:
        from utils import MLModelManager
        from config import MODEL_DIR
        
        manager = MLModelManager()
        print(f"  ✅ MLModelManager initialized")
        
        # Try loading a model
        model, meta = manager.load_model(
            MODEL_DIR / "cc_fraud_rf.pkl",
            MODEL_DIR / "cc_meta.json"
        )
        if model:
            print(f"  ✅ Model loading works")
            return True
        else:
            print(f"  ❌ Model loading failed")
            return False
    except Exception as e:
        print(f"  ❌ ML Manager error: {e}")
        return False

def check_predictions():
    """Verify prediction functions work"""
    print("\n🎯 Checking prediction engine...")
    try:
        from utils import calculate_fraud_features
        
        # Test fraud features
        features = calculate_fraud_features(
            amount=5000,
            hour=14,
            device="mobile",
            location="delhi"
        )
        
        if len(features) == 5:
            print(f"  ✅ Fraud features calculated: {features}")
        else:
            print(f"  ❌ Fraud features incorrect length")
            return False
        
        return True
    except Exception as e:
        print(f"  ❌ Prediction error: {e}")
        return False

def main():
    """Run all checks"""
    print("\n" + "="*60)
    print("🔍 FINANCIAL FRAUD DETECTION SYSTEM - VERIFICATION")
    print("="*60)
    
    results = {
        "Files": check_files(),
        "Imports": check_imports(),
        "Models": check_models(),
        "Config": check_config(),
        "Database": check_database(),
        "ML Manager": check_ml_manager(),
        "Predictions": check_predictions(),
    }
    
    print("\n" + "="*60)
    print("📊 VERIFICATION SUMMARY")
    print("="*60)
    
    for check, result in results.items():
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status:10} | {check}")
    
    all_pass = all(results.values())
    
    print("\n" + "="*60)
    if all_pass:
        print("✅ ALL CHECKS PASSED - System is ready to run!")
        print("   Start with: python app.py")
        print("   Access at: http://127.0.0.1:5000/")
    else:
        print("⚠️  SOME CHECKS FAILED - See details above")
        print("   Fix issues before running the application")
    print("="*60 + "\n")
    
    return 0 if all_pass else 1

if __name__ == "__main__":
    sys.exit(main())
