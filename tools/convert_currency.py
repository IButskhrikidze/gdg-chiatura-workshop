import requests

BASE_URL = "https://open.er-api.com/v6/latest"


def convert_currency(amount: float, from_currency: str, to_currency: str) -> dict:
    """
    Convert currency using live-ish rates from open.er-api.com (no key required, subject to terms).
    """
    from_currency = from_currency.upper().strip()
    to_currency = to_currency.upper().strip()

    if amount < 0:
        return {
            "status": "error",
            "error_message": "amount must be >= 0"
        }

    try:
        url = f"{BASE_URL}/{from_currency}"
        r = requests.get(url, timeout=10)
        r.raise_for_status()
        data = r.json()

        if data.get("result") != "success":
            return {
                "status": "error",
                "error_message": f"rate provider error: {data.get('error-type')}"
            }

        rates = data.get("rates", {})
        if to_currency not in rates:
            return {
                "status": "error",
                "error_message": f"unsupported target currency: {to_currency}"
            }

        rate = float(rates[to_currency])
        converted = float(amount) * rate

        return {
            "status": "success",
            "from_currency": from_currency,
            "to_currency": to_currency,
            "amount": amount,
            "rate": rate,
            "converted_amount": converted,
            "date": data.get("time_last_update_utc"),
            "source": "open.er-api.com",
        }

    except requests.RequestException as e:
        return {
            "status": "error",
            "error_message": f"network error: {e}"
        }
    except Exception as e:
        return {
            "status": "error",
            "error_message": f"unexpected error: {e}"
        }


if __name__ == '__main__':
    result = convert_currency(50.0, "GEL", "USD")
    print(result)
