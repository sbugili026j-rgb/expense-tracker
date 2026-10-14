import main


def test_save_and_load(tmp_path, monkeypatch):
    monkeypatch.setattr(main, "DATA_FILE", tmp_path / "expenses.json")
    data = [{"date": "2026-01-01", "amount": 5.0, "category": "food", "note": "lunch"}]
    main.save_expenses(data)
    assert main.load_expenses() == data


def test_load_when_file_missing(tmp_path, monkeypatch):
    monkeypatch.setattr(main, "DATA_FILE", tmp_path / "missing.json")
    assert main.load_expenses() == []


def test_totals_by_category(capsys):
    expenses = [
        {"date": "2026-01-01", "amount": 5.0, "category": "food", "note": ""},
        {"date": "2026-01-02", "amount": 3.0, "category": "food", "note": ""},
        {"date": "2026-01-03", "amount": 10.0, "category": "transport", "note": ""},
    ]
    main.show_totals(expenses)
    output = capsys.readouterr().out
    assert "food: 8.00" in output
    assert "transport: 10.00" in output
    assert "TOTAL: 18.00" in output


def test_delete_expense(tmp_path, monkeypatch):
    monkeypatch.setattr(main, "DATA_FILE", tmp_path / "expenses.json")
    expenses = [
        {"date": "2026-01-01", "amount": 5.0, "category": "food", "note": ""},
        {"date": "2026-01-02", "amount": 3.0, "category": "transport", "note": ""},
    ]
    monkeypatch.setattr("builtins.input", lambda _: "1")
    main.delete_expense(expenses)
    assert len(expenses) == 1
    assert expenses[0]["category"] == "transport"
