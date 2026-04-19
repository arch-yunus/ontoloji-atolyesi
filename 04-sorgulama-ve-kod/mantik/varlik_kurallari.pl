% Ontoloji Atölyesi: Varlık ve Mantık Kuralları
% Bu dosya, temel ontolojik sınıfları ve ilişkileri modeller.

% --- Sınıf Tanımları (Classes) ---
toz(insan).
toz(hayvan).
toz(bitki).

% --- Hiyerarşik İlişkiler (is_a) ---
canli(X) :- toz(X).
varlik(X) :- canli(X).

% --- Birey Tanımları (Individuals) ---
insan(sokrates).
insan(aristoteles).
hayvan(sarikiz).

% --- Özellikler ve İlişkiler (Properties) ---
bilge(aristoteles).
fani(X) :- canli(X).

% --- Ontolojik Sorgu Kuralları (Reasoning) ---
% "Varlık nedir?" sorgusu
nedir(X, varlik) :- varlik(X).

% "Kim fani?" sorgusu
kim_fani(X) :- fani(X).

% --- Örnek Sorgu Senaryosu ---
% ?- kim_fani(sokrates). -> true.
% ?- nedir(sarikiz, varlik). -> true.
