import torch
import torch.nn as nn
import timm


class AttentionBlock(nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.attn = nn.MultiheadAttention(dim, 8, batch_first=True)

    def forward(self, x):
        x, _ = self.attn(x, x, x)
        return x


class AquaFormerNet(nn.Module):

    def __init__(self, num_classes):
        super().__init__()

        # SAME AS TRAINING
        self.backbone = timm.create_model(
            "efficientnet_b0",
            pretrained=True,
            num_classes=0
        )

        dim = self.backbone.num_features

        self.attn = AttentionBlock(dim)

        encoder_layer = nn.TransformerEncoderLayer(
            d_model=dim,
            nhead=8,
            batch_first=True
        )

        self.transformer = nn.TransformerEncoder(
            encoder_layer,
            num_layers=2
        )

        self.fc = nn.Linear(dim, num_classes)

    def forward(self, x):

        x = self.backbone(x)

        x = x.unsqueeze(1)

        x = self.attn(x)

        x = self.transformer(x)

        x = x.mean(dim=1)

        x = self.fc(x)

        return x