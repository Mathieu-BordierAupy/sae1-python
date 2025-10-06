#!/usr/bin/env bash

exec pytest -v tests_explore_dnb.py::test_taux_reussite \
	tests_explore_dnb.py::test_meilleur \
	tests_explore_dnb.py::test_meilleur_taux_reussite \
	tests_explore_dnb.py::test_pire_taux_reussite \
	tests_explore_dnb.py::test_total_admis_presents \
	tests_explore_dnb.py::test_filtre_session \
	tests_explore_dnb.py::test_filtre_departement \
	tests_explore_dnb.py::test_filtre_college \
	tests_explore_dnb.py::test_string_contient
