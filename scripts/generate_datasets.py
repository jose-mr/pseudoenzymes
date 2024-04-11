
from uniprot.models import Entry, Keyword
import go.models as go
import eco.models as eco
import ec.models as ec
import cath.models as cath

def run():
    """run this script to generate the pseudoenzyme datasets"""

    # # Delete all UniProt previous entries and add new entries
    # Entry.objects.all().delete()
    # Keyword.objects.all().delete()
    # Entry.create_from_dat_file()


    # # Gene Ontology
    # go.Term.download_ontology()
    # go.Term.objects.all().delete()
    # go.Term.create_from_ontology_file()

    # go.Relation.objects.all().delete()
    # go.Relation.create_from_ontology_file()


    # # ECO Ontology
    # eco.Term.download_ontology()
    # eco.Term.objects.all().delete()
    # eco.Term.create_from_ontology_file()
    # eco.Relation.create_from_ontology_file()


    # # Link ontologies to UniProt entries
    # go.TermUniProtEntry.objects.all().delete() ff
    # go.TermUniProtEntry.create_from_gpa_file()


    # # EC numbers
    # ec.Entry.download_classes_file()
    # ec.Entry.download_ec_dat_file()
    # ec.Entry.objects.all().delete()
    # ec.Entry.create_classes_classes_files()
    # ec.Entry.create_entries_from_dat_file()

    # ec.Entry.download_intenz_xml_file()
    # ec.Synonym.objects.all().delete()
    # ec.Entry.create_synonyms_from_intenz_file()

    # # ec <-> uniprot associations
    # ec.EntryUniProtEntry.objects.all().delete()
    # ec.EntryUniProtEntry.create_from_uniprot_dat_file()


    # # CATH
    # cath.Superfamily.objects.all().delete()
    # cath.Superfamily.download_names_file()
    # cath.Superfamily.create_from_names_file()

    # CATH <-> UniProt associations
    cath.SuperfamilyUniprotEntry.objects.all().delete()

    cath.SuperfamilyUniprotEntry.create_from_interpro_file()

