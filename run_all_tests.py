import unittest

def run_tests():
    loader = unittest.TestLoader()
    suite = loader.discover('test', pattern='test_*.py')  # or 'tests' if renamed

    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    # Summary
    total = result.testsRun
    errors = len(result.errors)
    failures = len(result.failures)
    skipped = len(result.skipped)
    passed = total - errors - failures - skipped

    print("\n--- TEST SUMMARY ---")
    print(f"Total tests run   : {total}")
    print(f"✅ Passed          : {passed}")
    print(f"❌ Failures        : {failures}")
    print(f"⚠️ Errors          : {errors}")
    print(f"⏭️ Skipped         : {skipped}")

if __name__ == "__main__":
    run_tests()
