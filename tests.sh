#!/usr/bin/env bash

exec pytest tests_explore_dnb.py::test_taux_reussite \
	tests_explore_dnb.py::test_meilleur \
	tests_explore_dnb.py::test_meilleur_taux_reussite \
	tests_explore_dnb.py::test_pire_taux_reussite \
	tests_explore_dnb.py::test_total_admis_presents \
	tests_explore_dnb.py::test_filtre_session
