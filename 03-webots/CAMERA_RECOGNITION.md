# Camera recognition

Afin d'ajouter la reconnaissance d'objet sur une caméra, il sera nécessaire de modifier le fichier `PROTO` d'un robot.
Le prototype d'un robot s'édite via un clique droit sur l'objet en question. Il faudra ensuite sauvegarder, puis recharger le monde.

```bash
    # Trouver la définition de la caméra
    DEF EPUCK_CAMERA Camera {
      translation 0.03 0 0.028
      
      # ... beaucoup de lignes ...

      # Ajouter les lignes suivantes
      recognition Recognition {
          maxRange       100     # [0, inf)
          maxObjects     -1      # {-1, [0, inf)}
          occlusion      1       # {0, 1, 2}
          frameColor     1 0 0   # any color
          frameThickness 1       # [0, inf)
          segmentation   FALSE   # {TRUE, FALSE}
      }
    }
```